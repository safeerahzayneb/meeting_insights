import React from 'react'
import { Link } from 'react-router-dom';
import "./w3.css";

import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Breadcrumb from 'react-bootstrap/Breadcrumb'

import Jumbotron from 'react-bootstrap/Jumbotron'

async function uploadFile(file, meeting_name, date) {
    var formData = new FormData();
    
    formData.append('file', file);
    formData.append('name', meeting_name);
    formData.append('date', date);
    
    let response = await fetch('http://localhost:5000/upload',
        {
            method: 'POST',
            body: formData,
        });

    let data = await response.json();
    return data;
}

class SubmitForm extends React.Component {
    submitFormHandler = event => {
        event.preventDefault();
        uploadFile(this.refs.file.files[0], this.refs.date.value, this.refs.name.value)
        .then(data => console.log(data));
    }

	render() {
        return (
            <div>
<Container>
            <Row>
            <Col>
            <Breadcrumb>
  <Breadcrumb.Item href="localhost:3000">Home</Breadcrumb.Item>
  <Breadcrumb.Item active>Submit File</Breadcrumb.Item>
</Breadcrumb>

                <Jumbotron fluid>
  <Container>
    <h1>Meeting Insights</h1>
    <p>
      Making Quarantine efficiency = True efficency.
    </p>
  </Container>
</Jumbotron>
                <form onSubmit={this.submitFormHandler}>
                    <div>
                        Meeting Name: <input type="text" name="name" ref="name" />
                    </div>
                    <div>
                        Meeting Date: <input type="text" name="date" ref="date" />
                    </div>
                    <div>
                        <label>Upload Your File </label>
                        <input type="file" name="file" ref="file" className="form-control"/>
                    </div>
                    <input type="submit" value="Submit" />
                </form>
                <div>
                    <Link to="/menu" className="btn btn-primary">view menu</Link>
                </div>
            </Col>
            </Row>
            </Container>
            </div>
        );
    }
}

export default SubmitForm;