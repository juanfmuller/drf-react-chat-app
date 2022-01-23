import * as React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

import './App.css';
import SignIn from './signin.js';
import SignUp from './signup.js';
import MessageList from './messagelist';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<SignUp />}></Route>
        <Route path='/signin' element={<SignIn />}></Route>
        <Route path='/messages' element={<MessageList />}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
