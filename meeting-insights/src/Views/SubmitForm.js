import React from 'react'
import { Link } from 'react-router-dom';


class SubmitForm extends React.Component {
    submitFormHandler = event => {
        event.preventDefault();
        
        console.dir(this.refs.name.value); //will give us the name value
    }

	render() {
        return (
            <div>
                <form onSubmit={this.submitFormHandler}>
                    <div>
                        Meeting Name: <input type="text" name="name" ref="name" />
                    </div>
                    <div>
                        Meeting Date: <input type="text" name="date" ref="date" />
                    </div>
                </form>
                <div>
                    <Link to="/menu" className="btn btn-primary">view menu</Link>
                </div>
            </div>
        );
    }
}

export default SubmitForm;