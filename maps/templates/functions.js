// Function to get user's location
function getUserLocation() {
    return new Promise((resolve, reject) => {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const latitude = position.coords.latitude;
                    const longitude = position.coords.longitude;
                    resolve([latitude, longitude]); // Return as an array
                },
                (error) => {
                    reject(`Error retrieving location: ${error.message}`);
                }
            );
        } else {
            reject("Geolocation is not supported by this browser.");
        }
    });
}

function getDistance(lat1,long1,lat2,long2){
    var rad = 3958.8
    var val = acos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2)*cos(long2-long1))*rad
    return String(val)
}
