function Konversi() {
  var from = document.getElementById("from").value;
  var to = document.getElementById("to").value;
  var nilai = document.getElementById("nilai1").value;
  nilai = Number(nilai);
  const ProsesKonversi = (isiFrom,isiTo,Rumus) =>{
    if(from==isiFrom && to==isiTo){
    let hasil = document.getElementById("demo").innerHTML = `${nilai}° ${from} = ${Rumus}° ${to}`;
    return hasil;
    }
  };
  if(from==to){
    document.getElementById("demo").innerHTML = `${nilai}° ${from} = ${nilai}° ${to}`;
  }else if (from!=to){
    ProsesKonversi("Celcius","Reamur",nilai*4/5);
    ProsesKonversi("Celcius","Fahrenheit",nilai*9/5+32);
    ProsesKonversi("Celcius","Kelvin",nilai+273);
    ProsesKonversi("Reamur","Celcius",nilai*5/4);
    ProsesKonversi("Reamur","Fahrenheit",nilai*9/4+32);
    ProsesKonversi("Reamur","Kelvin",nilai*5/4+273);
    ProsesKonversi("Fahrenheit","Reamur",(nilai-32)*4/9);
    ProsesKonversi("Fahrenheit","Celcius",(nilai-32)*5/9);
    ProsesKonversi("Fahrenheit","Kelvin",(nilai-32)*5/9+273);
    ProsesKonversi("Kelvin","Celcius",nilai-273);
    ProsesKonversi("Kelvin","Fahrenheit",(nilai-273)*9/5+32);
    ProsesKonversi("Kelvin","Reamur",(nilai-273)*4/5);
  }
}