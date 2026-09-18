async function analyze(){
  const business = document.getElementById("business").value || "Your Business";
  const results = document.getElementById("results");
  results.textContent = "Analyzing...";
  const res = await fetch("/api/analyze", {
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body:JSON.stringify({business})
  });
  const data = await res.json();
  results.innerHTML = "<strong>"+data.business+"</strong><ul>" +
    data.insights.map(x => "<li>"+x+"</li>").join("") + "</ul>";
}
