Chart.defaults.global.legend.position = 'bottom'

var data = {
labels:['twitter-totalMentionsDegree','twitter-totalMentionsPageRank','twitter-totalMentionsKcore',],
datasets : [
{
label: 'JohnJHarwood',
backgroundColor: 'rgba(255,0,0,0.2)',
borderColor: 'rgba(255,0,0,1)',
borderWidth: 1,
fill:true,
data : [1,0.276926,1,]
},
{
label: 'Tweeter Average',
backgroundColor: 'rgba(0,255,0,0.2)',
borderColor: 'rgba(0,255,0,1)',
borderWidth: 1,
fill:true,
data : [0.0422652,0.031301,0.282431,]
},
]
}
var context = document.getElementById('Twitter-key-influencer-super-spreader-259395895-spider-chart').getContext("2d");
var chart = new Chart(context, {
		type: 'radar',
		data: data,
		options: {
				autowidth:false,
			scale: { ticks: { min:0, max:1, display:false}}
		}
});

