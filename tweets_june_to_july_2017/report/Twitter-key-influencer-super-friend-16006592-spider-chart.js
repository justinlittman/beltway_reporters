Chart.defaults.global.legend.position = 'bottom'

var data = {
labels:['totalDegreeCentrality','twitter-totalReciprocalMentionsUnweighted','twitter-reciprocalMentionsCliqueCount','kcore',],
datasets : [
{
label: 'BenjySarlin',
backgroundColor: 'rgba(255,0,0,0.2)',
borderColor: 'rgba(255,0,0,1)',
borderWidth: 1,
fill:true,
data : [0.295517,0.560976,0.26129,1,]
},
{
label: 'Tweeter Average',
backgroundColor: 'rgba(0,255,0,0.2)',
borderColor: 'rgba(0,255,0,1)',
borderWidth: 1,
fill:true,
data : [0.0264136,0.0588229,0.0100891,0.216108,]
},
]
}
var context = document.getElementById('Twitter-key-influencer-super-friend-16006592-spider-chart').getContext("2d");
var chart = new Chart(context, {
		type: 'radar',
		data: data,
		options: {
				autowidth:false,
			scale: { ticks: { min:0, max:1, display:false}}
		}
});

