
const crypt = (pilihan) => {
  if (pilihan == "dek") {
  document.getElementById("eod").innerHTML = `Liat pesan...`;
  let bEnk = document.getElementById("bEnk");
  bEnk.style.color = "black";
  bEnk.style.backgroundColor = "orange";
  let bDek = document.getElementById("bDek");
  bDek.style.color = "orange";
  bDek.style.backgroundColor = "black";
  document.getElementById("proses").innerHTML = `
    <label for="txt">Pesan: </label>
    <br/>
    <input type="text" name="txt" id="txt"/>
    <br/>
    <label for="key">kunci:</label>
    <br/>
    <input type="text" name="key" id="key" />
    <br/>
    <button type="submit" onclick="dek()">Lihat</button>
    <br/>
      `;
  }else{
    document.getElementById("eod").innerHTML = `Samarkan pesan...`;
    let bEnk = document.getElementById("bEnk");
    bEnk.style.color = "orange";
    bEnk.style.backgroundColor = "black";
    let bDek = document.getElementById("bDek");
    bDek.style.color = "black";
    bDek.style.backgroundColor = "orange";
    document.getElementById("proses").innerHTML = `
    <label for="txt">Pesan: </label>
    <br/>
    <input type="text" name="txt" id="txt"/>
    <br/>
    <label for="key">kunci:</label>
    <br/>
    <input type="text" name="key" id="key" />
    <br/>
    <button type="submit" onclick="enk()">Samarkan</button>
    <br/>
      `;
  }
}
const enk = () => {
  const txt = document.getElementById("txt").value;
  const key = document.getElementById("key").value;
  const cTxt = CryptoJS.AES.encrypt(txt, key);
  document.getElementById("hasil").innerHTML = `${cTxt}`;
}
const dek = () => {
  const txt = document.getElementById("txt").value;
  const key = document.getElementById("key").value;
  const bytes  = CryptoJS.AES.decrypt(txt.toString(), key);
  const pTxt = bytes.toString(CryptoJS.enc.Utf8);
  document.getElementById("hasil").innerHTML = `
  ${pTxt}
  `;
}
function CopyToClipboard(containerid) {
  document.getElementById(containerid).select();
  document.execCommand("copy");
}
const jedaCrypt = () => {
  setTimeout(function() {
    crypt();
  }, 1500);
}
