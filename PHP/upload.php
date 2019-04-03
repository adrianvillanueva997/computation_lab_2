<?php
include "validation.php";

if (isset($_POST['username'], $_POST['password'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];
    if (validation($username, $password)) {
        if (isset($_POST['project_id'], $_POST['user_id'], $_POST['model_id'], $_POST['file_content'])) {
            $project_id = $_POST['project_id'];
            $user_id = $_POST['user_id'];
            $model_id = $_POST['model_id'];
            $file_content = $_POST['file_content'];
            $directory_path = 'Data/' . $project_id . "/";
            $file_name = $directory_path . '/' . $model_id . '.model';
            if (!is_dir($directory_path)) {
                mkdir($directory_path);
            }
            $file_writer = fopen($file_name, 'wb+');
            fwrite($file_writer, $file_content);
            fclose($file_writer);
            echo "1";
        } else {
            echo "0";
        }
    } else {
        echo "0";
    }
}