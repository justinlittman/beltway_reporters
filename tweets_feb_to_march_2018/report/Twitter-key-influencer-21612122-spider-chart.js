Chart.defaults.global.legend.position = 'bottom'

var data = {
labels:['twitter-numberOfFollowers','twitter-wantsToBeInfluencer','twitter-actualInfluencer','twitter-trustedSource','twitter-mostMentioned','twitter-potentialReach','twitter-potentialConnectors','inDegreeCentrality','twitter-averageMentionsPerTweet',],
datasets : [
{
label: 'HotlineJosh',
backgroundColor: 'rgba(255,0,0,0.2)',
borderColor: 'rgba(255,0,0,1)',
borderWidth: 1,
fill:true,
data : [0.0249571,1,0.110866,0.259259,0.27439,0.473923,0.450606,1,0.101067,]
},
{
label: 'Tweeter Average',
backgroundColor: 'rgba(0,255,0,0.2)',
borderColor: 'rgba(0,255,0,1)',
borderWidth: 1,
fill:true,
data : [0.00858441,0.0495776,0.0115563,0.0338387,0.0403356,0.124321,0.0242427,0.0350748,0.0755588,]
},
]
}
var context = document.getElementById('Twitter-key-influencer-21612122-spider-chart').getContext("2d");
var chart = new Chart(context, {
		type: 'radar',
		data: data,
		options: {
				autowidth:false,
			scale: { ticks: { min:0, max:1, display:false}}
		}
});

