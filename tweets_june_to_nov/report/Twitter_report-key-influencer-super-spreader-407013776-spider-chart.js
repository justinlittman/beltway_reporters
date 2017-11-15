Chart.defaults.global.legend.position = 'bottom'

var data = {
labels:['twitter-totalMentionsDegree','twitter-totalMentionsPageRank','twitter-totalMentionsKcore',],
datasets : [
{
label: 'burgessev',
backgroundColor: 'rgba(255,0,0,0.2)',
borderColor: 'rgba(255,0,0,1)',
borderWidth: 1,
fill:true,
data : [0.616662,0.96455,1,]
},
{
label: 'Tweeter Average',
backgroundColor: 'rgba(0,255,0,0.2)',
borderColor: 'rgba(0,255,0,1)',
borderWidth: 1,
fill:true,
data : [0.0386347,0.0392736,0.319132,]
},
]
}
var context = document.getElementById('Twitter_report-key-influencer-super-spreader-407013776-spider-chart').getContext("2d");
var chart = new Chart(context, {
		type: 'radar',
		data: data,
		options: {
				autowidth:false,
			scale: { ticks: { min:0, max:1, display:false}}
		}
});

