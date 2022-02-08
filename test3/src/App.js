import axios from "axios";
import React, { Component } from "react";

import "./style.css";

const urlip = "http://localhost:3001/images/input.png";
const urlop = "http://localhost:3001/images/output.png";
const jnec = "http://localhost:3001/images/jnec.png";
class App extends Component {
    state = {
        selectedFile: null,
        detection: null,
    };

    // On file select (from the pop up)

    onFileChange = (event) => {
        // Update the state
        console.log(event.target.files[0]);
        this.setState({ selectedFile: event.target.files[0] });
    };

    // On file upload (click the upload button)

    onFileUpload = () => {
        // Create an object of formData
        const formData = new FormData();

        // Update the formData object
        formData.append(
            "file1",
            this.state.selectedFile,
            this.state.selectedFile.name
        );

        // Details of the uploaded file
        // console.log(this.state.selectedFile);

        // Request made to the backend api
        // Send formData object

        axios
            .post("http://192.168.5.191:5000/detect", formData)
            .then((response) => {
                this.setState({ detection: response });
                this.fileData();
            });
    };

    // File content to be displayed after
    // file upload is complete
    fileData = () => {
        console.log(this.state.detection);
        console.log("File :", this.state.selectedFile);
        if (this.state.selectedFile) {
            return ( <
                center >
                <
                div className = "myAlert"
                style = {
                    { marginTop: "25px" } } >
                <
                div className = "alert alert-success"
                role = "alert"
                style = {
                    { width: "500000px" } } >
                <
                div className = "" >
                <
                span > { " " } <
                b > { " " } <
                h5 > File Details: < /h5>{" "} <
                /b>{" "} <
                /span>{" "} <
                div className = "fs-6" >
                <
                tr > { " " } < span > { " " } < b > < td > File Name: < /td></b > { " " } <
                /span><td>{" "}{this.state.selectedFile.name}</td > < /tr> <
                tr > { " " } < span > { " " } < b > < td > File Type: < /td></b > { " " } < /span><td>{" "} { this.state.selectedFile.type } { " " } < /td></tr >
                <
                tr > { " " } < span > { " " } < b > < td > Last Modified: < /td></b > { " " } < /span><td>{"    "} { this.state.selectedFile.lastModifiedDate.toDateString() } { " " } < /td></tr >
                <
                /div>{" "} <
                /div>{" "} <
                /div>{" "} <
                /div>{" "} <
                /center>
            );
        } else {
            return ( <
                div >
                <
                br / > { " " } { /* <h4 className="text-white">Choose before Pressing the Upload button</h4> -->*/ } { " " } <
                /div>
            );
        }
    };

    footer = () => {
        return ( <
            center >
            <
            div >
            <
            div className = "team"
            style = {
                { textAlign: "center" } } >
            <
            br / > < h1 > Project Team < /h1>{" "} <
            p > { " " } <
            b >
            Abhishek Awasarmal < br / > Ganesh Dongre < br / > Rohit Magar { " " } <
            br / > Saurabh Tehare < br / >
            <
            /b>{" "} <
            /p>{" "} <
            h1 > Under the Guidance of < /h1>{" "} <
            p > { " " } <
            b > Prof.Priyanka Avhad < /b>{" "} <
            /p>{" "} <
            /div>{" "} <
            /div>{" "} <
            /center>
        );
    };

    render() {
        return ( <
            div >
            <
            center >
            <
            img style = {
                { paddingRight: "199px" } }
            src = { jnec }
            className = "jnecS"
            alt = "jnec" /
            >
            <
            h1 className = "myh1" > Ship Identification Using AI < /h1>{" "} <
            h4 className = "myh4" > Upload Image
            for detection < /h4> <br / >
            <
            input style = {
                { border: "2px" } }
            className = "myinputfile"
            type = "file"
            onChange = { this.onFileChange }
            />{" "} <
            button disabled = {!this.state.selectedFile }
            className = "btn btn-outline-danger button"
            onClick = { this.onFileUpload } >
            { " " }
            Upload { " " } <
            /button>{" "} <
            /center>{" "} { this.fileData() } { " " } <
            center >
            <
            div className = "container-fluid" >
            <
            div className = "row" >
            <
            div className = "col-2 offset-4"
            style = {
                { marginTop: "5px", alignItems: "center" } } >
            <
            h6 className = "Input text-danger" > Input < /h6> <br / >
            <
            img style = {
                {
                    height: "250px",
                    width: "250px",
                    marginTop: "5px",
                    alignItems: "center",
                }
            }
            src = { urlip }
            alt = "op"
            className = "imgIn" /
            >
            <
            /div>{" "} <
            div className = "col-2"
            style = {
                {
                    marginLeft: "60px",
                    marginTop: "5px",
                    alignItems: "center",
                }
            } >
            <
            h6 className = "Output text-danger" > Output < /h6> <br / >
            <
            img style = {
                { height: "250px", width: "250px", marginTop: "5px" } }
            src = { urlop }
            alt = "op"
            className = "imgOp" /
            >
            <
            /div>{" "} <
            div > < /div>{" "} <
            /div>{" "} <
            /div>{" "} <
            /center>{" "} { this.footer() } { " " } <
            /div>
        );
    }
}

export default App;