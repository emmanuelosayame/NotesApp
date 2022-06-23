import React from 'react';
import * as ReactDOM from 'react-dom/client'
import './index.css';
import App from './App';
import {  ChakraProvider } from '@chakra-ui/react'



const rootElement = document.getElementById('root');
ReactDOM.createRoot(rootElement).render(
  <React.StrictMode>
    <ChakraProvider  >
      <App />
    </ChakraProvider>
  </React.StrictMode>,
);

