Chart.defaults.global.legend.position = 'bottom'

var data = {
labels:['totalDegreeCentrality','twitter-totalReciprocalMentionsUnweighted','twitter-reciprocalMentionsCliqueCount','kcore',],
datasets : [
{
label: 'AaronMehta',
backgroundColor: 'rgba(255,0,0,0.2)',
borderColor: 'rgba(255,0,0,1)',
borderWidth: 1,
fill:true,
data : [1,0.28777,0.114286,0.846154,]
},
{
label: 'Tweeter Average',
backgroundColor: 'rgba(0,255,0,0.2)',
borderColor: 'rgba(0,255,0,1)',
borderWidth: 1,
fill:true,
data : [0.0367475,0.0452622,0.0114633,0.259531,]
},
]
}
var context = document.getElementById('Twitter-key-influencer-super-friend-103016675-spider-chart').getContext("2d");
var chart = new Chart(context, {
		type: 'radar',
		data: data,
		options: {
				autowidth:false,
			scale: { ticks: { min:0, max:1, display:false}}
		}
});

