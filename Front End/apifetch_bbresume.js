const countEl = document.getElementById('count');


updateVisitCount();
//Testinglllll
function updateVisitCount() {
    fetch('https://8zsb3och04.execute-api.us-east-2.amazonaws.com/Prod')
        .then(response => {
        return response.json()
      })
        .then(data => {
            console.log(data)
			document.getElementById('count').innerHTML = JSON.stringify(data.body['vc']);
        })
    }
	
	
