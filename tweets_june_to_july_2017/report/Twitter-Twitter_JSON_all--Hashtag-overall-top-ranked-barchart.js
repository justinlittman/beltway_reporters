Chart.defaults.global.legend.position = 'bottom'

var data = {
labels:['breaking','Obamacare','SCOTUS','Trumpcare','GA06','pharma',],
datasets : [
{
label: 'Hashtag (Twitter JSON all)',
backgroundColor: 'rgba(255,0,0,0.2)',
borderColor: 'rgba(255,0,0,1)',
borderWidth: 1,
data : [50,50,50,50,50,50,]
},
]
}
var context = document.getElementById('Twitter-Twitter_JSON_all--Hashtag-overall-top-ranked-barchart').getContext("2d");
var chart = new Chart(context, {
		type: 'bar',
		data: data,
		options: {
			autowidth:false,
			scales: {
			yAxes: [{
				ticks: {
					beginAtZero:true
				}
			}]
		}
	}
});

