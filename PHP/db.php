<?php
/**
 * connect_to_db
 *
 * @return $conn
 */
function connect_to_db()
{
    $servername = "";
    $username = "";
    $password = "";
    $database = "";

    $conn = new mysqli($servername, $username, $password, $database);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
        return null;
    }
    return $conn;
}

