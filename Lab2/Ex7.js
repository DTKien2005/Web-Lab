function handleBlur(){
    alert("Field1 lost focus!");
}
const field1 = document.getElementById("field1");

field1.addEventListener("blur", handleBlur);