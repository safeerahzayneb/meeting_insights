import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import * as serviceWorker from './serviceWorker';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import App from './App';
import SubmitForm from './Views/SubmitForm';
import MenuViewer from './Views/MenuViewer'

const routing = (
  <BrowserRouter>
      <div className="page">
          <Switch>
              <Route exact path="/" component={App} />
              <Route exact path="/submit" component={SubmitForm} />
              <Route exact path="/menu" component={MenuViewer} />
          </Switch>
      </div>
  </BrowserRouter>
)
ReactDOM.render(routing, document.getElementById('root'));


// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
