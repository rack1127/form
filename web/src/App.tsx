import { useState } from 'react';
import './App.css';
import QRCode from 'qrcode'



function App() {
    const [value, setValue] = useState("");
    const [qrcode, setQrcode] = useState("");
    
    const change_display = () => {
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

    const createQrcode: React.FormEventHandler = async (event) => {
        event.preventDefault();
        const form = Object.fromEntries(new FormData(event.target as HTMLFormElement));
        const json_form = JSON.stringify(form)
        const qrcode =  QRCode.toDataURL(json_form, {type: "image/png"})
        setQrcode(await qrcode)
    };


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
            <div><img src= {qrcode}/></div>
        </form>
    </>
  )
}

export default App
