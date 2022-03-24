import logo from './logo.svg';
import './App.css';
import { useTranslation } from "react-i18next";
import chineseResource from './chinese.json';

function App() {
  const { t, i18n } = useTranslation();
  const load = () => {
    i18n.addResourceBundle("cn", "translation", chineseResource);
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
          {t("welcome")}
        </a>
      </header>
      <div>
        <button onClick={() => i18n.changeLanguage("fr")}>French</button>
        <button onClick={() => i18n.changeLanguage("en")}>English</button>
        <button onClick={() => i18n.changeLanguage("cn")}>Chinese</button>
        <button onClick={() => load()}>Load Chinese</button>

      </div>
    </div>
  );
}

export default App;
