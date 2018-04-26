Chart.defaults.global.legend.position = 'bottom'

var data = {
labels:['BREAKING','pharma','MarchForOurLives','PA18','FDA','biotech',],
datasets : [
{
label: 'Hashtag (Twitter JSON all_filtered)',
backgroundColor: 'rgba(255,0,0,0.2)',
borderColor: 'rgba(255,0,0,1)',
borderWidth: 1,
data : [50,50,50,50,50,50,]
},
]
}
var context = document.getElementById('Twitter-Twitter_JSON_all_filtered--Hashtag-overall-top-ranked-barchart').getContext("2d");
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

