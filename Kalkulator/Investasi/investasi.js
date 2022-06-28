function Saham(modal,labaDalamPersen,lamaSaham,profitPer) {
  let profit = labaDalamPersen/100+1;
  if (profitPer=="Bulan"){
    let lamaHariSaham = lamaSaham*30;
    let bulan = lamaHariSaham/30;
    profit **= bulan;
    let hasil = modal*profit;
    console.log(hasil);
  }
  if (profitPer=="Tahun"){
    let lamaHariSaham = lamaSaham*365;
    let tahun = lamaHariSaham/365;
    profit **= tahun;
    let hasil = modal*profit;
    console.log(hasil);
  }
}
let modal = 1000;
profit= 10;
lama = 1;
waktu = "Bulan";
Saham(modal,profit,lama,waktu);