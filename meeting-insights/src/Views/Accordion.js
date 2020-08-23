import React from 'react'
import Accordion from 'react-bootstrap/Accordion'
import Card from 'react-bootstrap/Card'

export default class Acordion extends React.Component {
  render() {
    return (
      <Accordion>
        <Card bg={'primary'} style={{
            color: 'white',
        }}>
            <Card.Header><h2>Meeting Info</h2></Card.Header>
            <Card.Body>
                <p>Date:</p>
                <p>Attendees:</p>
            </Card.Body>
        </Card>
        <Card>
          <Accordion.Toggle as={Card.Header} eventKey="1">
            Transcript
          </Accordion.Toggle>
          <Accordion.Collapse eventKey="1">
            <Card.Body>Hello! I'm the transcript</Card.Body>
          </Accordion.Collapse>
        </Card>
        <Card>
          <Accordion.Toggle as={Card.Header} eventKey="2">
            Summary
          </Accordion.Toggle>
          <Accordion.Collapse eventKey="2">
            <Card.Body>Hello! I'm the summary</Card.Body>
          </Accordion.Collapse>
        </Card>
        <Card>
          <Accordion.Toggle as={Card.Header} eventKey="3">
            Key Phrases
          </Accordion.Toggle>
          <Accordion.Collapse eventKey="3">
            <Card.Body>Hello! I'm the key phrases</Card.Body>
          </Accordion.Collapse>
        </Card>
      </Accordion>
    )
  }
}
