import React from 'react'

import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import ListGroup from 'react-bootstrap/ListGroup'
import Tab from 'react-bootstrap/Tab'

import Accordion from './Accordion'

export default class MenuViewer extends React.Component {
  render() {
    return (
      <Container>
        <Row
          style={{
            height: 150,
            alignItems: 'center',
            justifyContent: 'center',
          }}
        >
          <h1>View Meetings</h1>
        </Row>
        <Row
          style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
          }}
        >
          <Col>
            <Tab.Container
              id="list-group-tabs-example"
              defaultActiveKey="#link1"
            >
              <Row>
                <Col sm={4}>
                  <ListGroup>
                    <ListGroup.Item action href="#meeting1">
                      Meeting 1: Planning
                    </ListGroup.Item>
                    <ListGroup.Item action href="#meeting2">
                      Meeting 2: Ideation
                    </ListGroup.Item>
                    <ListGroup.Item action href="#meeting3">
                      Meeting 3: Project Meeting
                    </ListGroup.Item>
                    <ListGroup.Item action href="#meeting4">
                      Meeting 4: Check-in
                    </ListGroup.Item>
                    <ListGroup.Item action href="#meeting5">
                      Meeting 5: Review
                    </ListGroup.Item>
                  </ListGroup>
                </Col>
                <Col sm={8}>
                  <Tab.Content>
                    <Tab.Pane eventKey="#meeting1">
                      <Accordion />
                    </Tab.Pane>
                    <Tab.Pane eventKey="#meeting2">
                      <Accordion />
                    </Tab.Pane>
                    <Tab.Pane eventKey="#meeting3">
                      <Accordion />
                    </Tab.Pane>
                    <Tab.Pane eventKey="#meeting4">
                      <Accordion />
                    </Tab.Pane>
                    <Tab.Pane eventKey="#meeting5">
                      <Accordion />
                    </Tab.Pane>
                  </Tab.Content>
                </Col>
              </Row>
            </Tab.Container>
          </Col>
        </Row>
      </Container>
    )
  }
}
