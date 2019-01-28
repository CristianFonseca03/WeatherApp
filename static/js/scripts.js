var map, infoWindow;
var Bogota = [4.60971, -74.08174], Tokyo = [35.6894, 139.692], Paris = [48.85340, 2.34860],
    Washington = [38.9041, -77.0171];
var array_markers = new Array();

function deleter_markers() {
    if (array_markers.length > 0) {
        array_markers[0].setMap(null);
    }
    array_markers = [];
}

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 5.69702, lng: 5.69702},
        zoom: 6
    });
    if (navigator.geolocation) {
        deleter_markers();
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
            array_markers.push(marker);
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
            array_markers.push(marker);
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

$("#bogota").click(function (e) {
    deleter_markers();
    $("#lat").val(Bogota[0]);
    $("#lon").val(Bogota[1]);
    var pos = {
        lat: Bogota[0],
        lng: Bogota[1]
    };
    map.setCenter(pos);
    map.setZoom(10);
    var marker = new google.maps.Marker({
        position: pos,
        map: map,
        title: "Bogota",
        animation: google.maps.Animation.DROP
    });
    array_markers.push(marker);
});
$("#tokyo").click(function (e) {
    $("#lat").val(Tokyo[0]);
    $("#lon").val(Tokyo[1]);
    var pos = {
        lat: Tokyo[0],
        lng: Tokyo[1]
    };
    map.setCenter(pos);
    map.setZoom(10);
    var marker = new google.maps.Marker({
        position: pos,
        map: map,
        title: "Tokyo",
        animation: google.maps.Animation.DROP
    });
    array_markers.push(marker);
});
$("#paris").click(function (e) {
    $("#lat").val(Paris[0]);
    $("#lon").val(Paris[1]);
    var pos = {
        lat: Paris[0],
        lng: Paris[1]
    };
    map.setCenter(pos);
    map.setZoom(10);
    var marker = new google.maps.Marker({
        position: pos,
        map: map,
        title: "Paris",
        animation: google.maps.Animation.DROP
    });
    array_markers.push(marker);
});
$("#washington").click(function (e) {
    $("#lat").val(Washington[0]);
    $("#lon").val(Washington[1]);

    var pos = {
        lat: Washington[0],
        lng: Washington[1]
    };
    map.setCenter(pos);
    map.setZoom(10);
    var marker = new google.maps.Marker({
        position: pos,
        map: map,
        title: "Washington",
        animation: google.maps.Animation.DROP
    });
    array_markers.push(marker);
});