chrome.action.onClicked.addListener((tab) => {
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    func: getCommentsAndAnalyze
  });
});

function getCommentsAndAnalyze() {
  let comments = [...document.querySelectorAll('.comment-text')].map(comment => comment.innerText);
  fetch('http://localhost:8000/analyze_sentiment/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ text: comments.join(" ") })
  })
  .then(response => response.json())
  .then(data => alert("Sentiment Analysis Result: " + data.sentiment));
}