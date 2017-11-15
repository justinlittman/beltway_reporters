Chart.defaults.global.legend.position = 'bottom'

var data = {
labels:['totalDegreeCentrality','twitter-totalReciprocalMentionsUnweighted','twitter-reciprocalMentionsCliqueCount','kcore',],
datasets : [
{
label: 'jaketapper',
backgroundColor: 'rgba(255,0,0,0.2)',
borderColor: 'rgba(255,0,0,1)',
borderWidth: 1,
fill:true,
data : [0.577716,0.852018,0.405381,1,]
},
{
label: 'Tweeter Average',
backgroundColor: 'rgba(0,255,0,0.2)',
borderColor: 'rgba(0,255,0,1)',
borderWidth: 1,
fill:true,
data : [0.0371956,0.0576048,0.00757939,0.253068,]
},
]
}
var context = document.getElementById('Twitter_report-key-influencer-super-friend-14529929-spider-chart').getContext("2d");
var chart = new Chart(context, {
		type: 'radar',
		data: data,
		options: {
				autowidth:false,
			scale: { ticks: { min:0, max:1, display:false}}
		}
});
