import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1> P2P Messaging App </h1>
      </header>
      <main>

      <div id = "chat-window">
      </div>

      <div id = "message-input">
        <input type="text" placeholder = "You: " />
        <button>Send</button>

      </div>


      </main>
    </div>
  );
}

export default App;
