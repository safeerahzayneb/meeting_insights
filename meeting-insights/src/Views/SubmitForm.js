import React from 'react'
import { Link } from 'react-router-dom';

function uploadFile(file, meeting_name, date) {
    var formData = new FormData();
    
    formData.append('file', file)
    formData.append('name', meeting_name);
    formData.append('date', date);
    
    fetch('http://localhost:5000/upload', {
      // content-type header should not be specified!
      method: 'POST',
      body: formData,
      mode: 'no-cors',
    })
      .then(response => response.json())
      .then(success => {
        // Do something with the successful response
      })
      .catch(error => console.log(error)
    );
}

class SubmitForm extends React.Component {
    submitFormHandler = event => {
        event.preventDefault();
        
        console.dir(this.refs.name.value); //will give us the name value
        uploadFile(this.refs.file.files[0], this.refs.date.value, this.refs.name.value)
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
                    <div>
                        <label>Upload Your File </label>
                        <input type="file" name="file" ref="file" className="form-control"/>
                    </div>
                    <input type="submit" value="Submit" />
                </form>
                <div>
                    <Link to="/menu" className="btn btn-primary">view menu</Link>
                </div>
            </div>
        );
    }
}

export default SubmitForm;