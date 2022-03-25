import logo from './logo.svg';
import './App.css';
import { useTranslation } from "react-i18next";
import chineseResource from './Translation/zh.json';


function App() {  
  const { t, i18n } = useTranslation(["common"]);
  //const { t, i18n } = useTranslation(["uncommon"]);
  //{t("welcome")} 
  const load = () => {
    i18n.addResourceBundle("zh", "common", chineseResource);
  }
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          {t("welcome1")}  
        
        </a>
      </header>
      
      <div>     
        
        <button onClick={() => i18n.changeLanguage("fr")}>{t("button1")}</button>
        <button onClick={() => i18n.changeLanguage("en")}>{t("button2")}</button>
        <button onClick={() => i18n.changeLanguage("zh")}>{t("button3")}</button>
        <button onClick={() => load()}>{t("button4")}</button>

      </div>
    </div>
  );
}

export default App;
