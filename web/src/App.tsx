import { useState } from 'react';
import './App.css';

function App() {
    const [value, setValue] = useState("");
    
    const change_display = () => {
        console.log(value);
        if(value === 'seito'){
            return (<div id="seito">
                氏名：<input type="text" name="seito_yourname" id="name"/><br/>
                学籍番号：<input type="tell"name="seito_schoolnumber"id="school"/><br/>
                電話番号：<input type="tell" name="seito_phonenumber"id="phone"/><br/>
                <button type="submit" value="ボタン">作成</button>
            </div>);
        }
        else if(value === 'ippan'){
            return (<div id="ippan">
                氏名：<input type="text" name="ippan_yourname"/><br/>
                電話番号：<input type="tell"name="ippan_phonenumber"/><br/>
                住んでいる地域：<input type="text" name="ippan_yourplace"/><br/>
                <button type="submit" value="ボタン">作成</button>
            </div>);
        }
        else if(value === 'hogosya'){
            return (<div id = "hogosya">
                氏名：<input type="text" name="hogosya_yourname"/><br/>
                お子様の氏名：<input type="text" name="kids_yourname"/><br/>
                お子様の学籍番号：<input type="tell"name="kids_schoolnumber"/><br/>
                電話番号：<input type="tell" name="hogosya_yourname"/><br/>
                <button type="submit" value="ボタン">作成</button>
            </div>);
        }
    }


    const selectChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
        const value = e.target.value;
        setValue(value);
    };

    const createQrcode: React.FormEventHandler = (event) => {
        event.preventDefault();
        const form = Object.fromEntries(new FormData(event.target as HTMLFormElement));
        // const seito = form.get("seito_yourname")
        console.log(form);
        
        // list = $('form').serializeArray();
        // list = JSON.stringify(parseJson(list))
        // var qr = new QRious({value: list});
        // var png = qr.toDataURL();
        // document.getElementById("newImg").src = png;
    };

    // const parseJson = (form) => {
    //     var returnJson = {}
    //     form.map((list) => returnJson[list.name] = Encoding.convert(list.value, "utf-8"))
    //     let utf8Encode = new TextEncoder(); 
    //     // 文字列をバイト配列にエンコードする
    //     let byteArray = utf8Encode.encode(returnJson.yourname);
    //     return returnJson
    // }

    return (
        <>
        <h1>情報登録フォーム</h1>
        <form onSubmit={createQrcode}>
            <label id = 'type'>分類:</label>
            <select defaultValue={""} name = "syurui" id="syurui"  onChange={e => selectChange(e)}>
                <option value="" selected hidden>選択してください</option>
                <option value="ippan">一般</option>
                <option value="seito">生徒</option>
                <option value="hogosya">生徒保護者</option>
            </select><br/>
            {change_display()}
        </form>
        <p id="output-message"></p>
        <div><img id="newImg"/></div>
    </>
  )
}

export default App
