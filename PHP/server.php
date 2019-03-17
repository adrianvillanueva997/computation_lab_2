<?php
include "validation.php";
if (isset($_POST["username"]) && isset($_POST["password"])) {
    $username = $_POST["username"];
    $password = $_POST["password"];
    if (validation($username, $password)) {
        if (isset($_POST["project_id"]) && isset($_POST["user_id"]) && isset($_POST["user_id"])
            && isset($_POST["model_id"])) {
            $project_id = $_POST["project_id"];
            $user_id = $_POST["user_id"];
            $model_id = $_POST["model_id"];
            $directory_path = "Data/" . $project_id . "/";
            if (isset($_POST["file_content"])) {
                // == DOWNLOAD FILE ==
                // 1. Verify if working directory exists
                // 2. If the directory doesn't exist, there is nothing to download
                // 3. If the directory, exists, try to read the POST binary stuff
                // 4. Write the file remotely
                if (is_dir($directory_path)) {
                    $file_content = $_POST["file_content"];
                    $file_name = $directory_path . "/" . $model_id . ".model";
                    $file_writer = fopen($file_name, "w+");
                    fwrite($file_writer, $file_content);
                    fclose($file_writer);
                    echo "1";
                } else {
                    echo "0";
                }
            } else {
                // == UPLOAD FILE ==
                //1. Verify if project directory exists
                //2. Read file
                //3. Send it to python
                if (is_dir($directory_path)) {
                    $file = $directory_path . "/" . $model_id . ".model";
                    $content = file_get_contents($file);
                    echo $content;
                } else {
                    echo "0";
                }
            }
        }
    }
}