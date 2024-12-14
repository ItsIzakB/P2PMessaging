import logo from './logo.svg';
import './App.css';
import ChatWindow from "./ChatWindow";
import {io} from "socket.io-client";

function App() {
  const[messages, setMessages] = useState([]);
  const[input, setInput] = useState("");
  
  useEffect(() => {
    
  })



  return (
    <div className="App">
      <header className="App-header">
        <h1> P2P Messaging App </h1>
      </header>
      <main>

      <div id = "chat-window">
      </div>

      <div id = "message-input">
        <input type="text" placeholder = "Write a message" />
        <button>Send</button>

      </div>


      </main>
    </div>
  );
}

export default App;
