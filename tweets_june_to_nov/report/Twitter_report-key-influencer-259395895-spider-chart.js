Chart.defaults.global.legend.position = 'bottom'

var data = {
labels:['twitter-numberOfFollowers','twitter-wantsToBeInfluencer','twitter-actualInfluencer','twitter-trustedSource','twitter-mostMentioned','twitter-potentialReach','twitter-potentialConnectors','inDegreeCentrality','twitter-averageMentionsPerTweet',],
datasets : [
{
label: 'JohnJHarwood',
backgroundColor: 'rgba(255,0,0,0.2)',
borderColor: 'rgba(255,0,0,1)',
borderWidth: 1,
fill:true,
data : [0.0751578,0.82058,0.109598,0.547458,0.527616,0.468486,0.776688,0.993361,0.0930044,]
},
{
label: 'Tweeter Average',
backgroundColor: 'rgba(0,255,0,0.2)',
borderColor: 'rgba(0,255,0,1)',
borderWidth: 1,
fill:true,
data : [0.00765489,0.0685429,0.00633265,0.0440301,0.0530911,0.134539,0.0350789,0.0383236,0.0663142,]
},
]
}
var context = document.getElementById('Twitter_report-key-influencer-259395895-spider-chart').getContext("2d");
var chart = new Chart(context, {
		type: 'radar',
		data: data,
		options: {
				autowidth:false,
			scale: { ticks: { min:0, max:1, display:false}}
		}
});

