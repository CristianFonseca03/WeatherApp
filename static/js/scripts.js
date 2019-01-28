var map, infoWindow;
var Bogota = [4.60971, -74.08174], Tokyo = [35.6894, 139.692], Paris = [2.34860, 48.85340],
    Washington = [38.9041, -77.0171];

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 5.69702, lng: 5.69702},
        zoom: 6
    });
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            var pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
            map.setCenter(pos);
            var marker = new google.maps.Marker({
                position: pos,
                map: map,
                icon: {
                    path: google.maps.SymbolPath.CIRCLE,
                    scale: 10
                },
            });
            document.getElementById("lat").value = (position.coords.latitude).toPrecision(6);
            document.getElementById("lon").value = (position.coords.longitude).toPrecision(6);
        }, function () {
            handleLocationError(true, infoWindow, map.getCenter());
        });
    } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
    }
    var marker;

    function placeMarker(location) {
        document.getElementById("lat").value = (location.lat()).toPrecision(6);
        document.getElementById("lon").value = (location.lng()).toPrecision(6);
        if (marker) {
            marker.setPosition(location);
        } else {
            marker = new google.maps.Marker({
                position: location,
                map: map
            });
        }
    }

    google.maps.event.addListener(map, 'click', function (event) {
        placeMarker(event.latLng);
    });
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    infoWindow.setPosition(pos);
    infoWindow.setContent(browserHasGeolocation ?
        'Error: The Geolocation service failed.' :
        'Error: Your browser doesn\'t support geolocation.');
    infoWindow.open(map);
}


