import React from 'react'
import { Link } from 'react-router-dom'
import './w3.css'

import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Breadcrumb from 'react-bootstrap/Breadcrumb'
import Spinner from 'react-bootstrap/Spinner'

// import Jumbotron from 'react-bootstrap/Jumbotron'

async function uploadFile(file, meeting_name, date) {
  var formData = new FormData()

  formData.append('file', file)
  formData.append('name', meeting_name)
  formData.append('date', date)

  let response = await fetch('http://localhost:5000/upload', {
    method: 'POST',
    body: formData,
  })

  let data = await response.json()
  return data
}

class SubmitForm extends React.Component {
  submitFormHandler = (event) => {
    event.preventDefault()
    uploadFile(
      this.refs.file.files[0],
      this.refs.date.value,
      this.refs.name.value,
    ).then((data) => console.log(data))
  }

  render() {
    return (
      <div>
        <Container>
          <Row>
            <Container
              style={{
                height: 150,
                justifyContent: 'center',
                alignItems: 'center',
                paddingTop: 50,
                paddingBottom: 80,
                marginBottom: 50,
                color: 'white',
              }}
            >
              <h1>Insightful Meetings</h1>
              <h3>Making Quarantine efficiency = True efficiency.</h3>
            </Container>
            <Col>
              {/* <Breadcrumb>
                <Breadcrumb.Item href="localhost:3000">Home</Breadcrumb.Item>
                <Breadcrumb.Item active>Submit File</Breadcrumb.Item>
              </Breadcrumb> */}

              {/* <Container> */}

              {/* </Jumbotron> */}
              <form onSubmit={this.submitFormHandler}>
                <div style={{ paddingBottom: 10 }}>
                  Meeting Name: <input type="text" name="name" ref="name" />
                </div>
                <div>
                  Meeting Date: <input type="text" name="date" ref="date" />
                </div>
                <Col>
                  <div style={{ padding: 20 }}>
                    <label>Upload Your .mp4 File </label>
                    <input
                      type="file"
                      name="file"
                      ref="file"
                      className="form-control"
                    />
                  </div>
                </Col>
                {/* <Spinner animation="grow" /> */}
                <Col>
                  <div></div>
                </Col>
                <input type="submit" value="Submit" style={{ margin: 10 }} />
              </form>
              <div>
                <Link to="/menu" className="btn btn-primary">
                  View Your Meetings →
                </Link>
              </div>
            </Col>
          </Row>
        </Container>
      </div>
    )
  }
}

export default SubmitForm
