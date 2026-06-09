const countries = ["India","USA","Germany","Australia","Japan"];
const dataList = document.getElementById("dataList");

for( name of countries ){
    dataList.innerHTML += `<li>${name}</li>`;
}

