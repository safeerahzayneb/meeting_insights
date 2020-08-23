import React from 'react'
import { Link } from 'react-router-dom';
import "./w3.css";

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
<header class="w3-container w3-red">
  <h1>Header</h1>
</header>
            <nav class="w3-bar w3-black">
  <a href="#home" class="w3-button w3-bar-item">Home</a>
  <a href="#band" class="w3-button w3-bar-item">Band</a>
  <a href="#tour" class="w3-button w3-bar-item">Tour</a>
  <a href="#contact" class="w3-button w3-bar-item">Contact</a>
</nav>

                <h2> test </h2>
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