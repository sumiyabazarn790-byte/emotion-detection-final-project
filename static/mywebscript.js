function runEmotionAnalysis() {
  const textToAnalyze = document.getElementById("textToAnalyze").value;
  const responseTarget = document.getElementById("system_response");
  const request = new XMLHttpRequest();

  request.onreadystatechange = function handleResponse() {
    if (request.readyState === 4) {
      responseTarget.innerHTML = request.responseText;
    }
  };

  request.open(
    "GET",
    `/emotionDetector?textToAnalyze=${encodeURIComponent(textToAnalyze)}`,
    true
  );
  request.send();
}
