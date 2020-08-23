import React from 'react'
import Accordion from 'react-bootstrap/Accordion'
import Card from 'react-bootstrap/Card'


export default class Acordion extends React.Component {
  constructor() {
    super();
    this.state = { data: [] };
  }
  async componentDidMount() {
    const response = await fetch(`http://localhost:5000/meeting/1`);
    const json = await response.json();
    this.setState({ data: json });
  }
  render() {
    return (
      <Accordion>
        <Card
          bg={'primary'}
          style={{
            color: 'white',
          }}
        >
          <Card.Header>
            <h2>Meeting Info</h2>
            <i>Meeting Id: {this.state.data["meeting_id"]}</i>
          </Card.Header>
          <Card.Body>
            <p><b>Date:</b> {this.state.data["date"]}</p>
            <p><b>Attendees:</b> {this.state.data["attendees"]}</p>
          </Card.Body>
        </Card>
        <Card>
          <Accordion.Toggle as={Card.Header} eventKey="1">
            <b>Summary</b>
          </Accordion.Toggle>
          <Accordion.Collapse eventKey="1">
            <Card.Body>{this.state.data["summary"]}</Card.Body>
          </Accordion.Collapse>
        </Card>
        <Card>
          <Accordion.Toggle as={Card.Header} eventKey="2">
            <b>Key Phrases</b>
          </Accordion.Toggle>
          <Accordion.Collapse eventKey="2">
            <Card.Body>{this.state.data["key_phrases"]}</Card.Body>
          </Accordion.Collapse>
        </Card>
        <Card>
          <Accordion.Toggle as={Card.Header} eventKey="3">
            <b>Sentiment Analysis</b>
          </Accordion.Toggle>
          <Accordion.Collapse eventKey="3">
            <Card.Body>{this.state.data["sentiment_analysis"]}</Card.Body>
          </Accordion.Collapse>
        </Card>
        <Card>
          <Accordion.Toggle as={Card.Header} eventKey="4">
            <b>Entity Recognition</b>
          </Accordion.Toggle>
          <Accordion.Collapse eventKey="4">
            <Card.Body>
              {this.state.data["entity_recog"]}
            </Card.Body>
          </Accordion.Collapse>
        </Card>
        <Card>
          <Accordion.Toggle as={Card.Header} eventKey="5">
            <b>Entity Linking</b>
          </Accordion.Toggle>
          <Accordion.Collapse eventKey="5">
            <Card.Body>
              {this.state.data["entity_linking"]}
            </Card.Body>
          </Accordion.Collapse>
        </Card>
      </Accordion>
    )
  }
}
