<?php
include 'validation.php';

if (isset($_POST['username'], $_POST['password'])) {
    error_reporting(E_ALL);
    ini_set('display_errors', '1');
    $username = $_POST['username'];
    $password = $_POST['password'];
    if (validation($username, $password)) {
        if (isset($_POST['project_id'], $_POST['model_id'])) {
            $project_id = $_POST['project_id'];
            $model_id = $_POST['model_id'];
            $directory_path = 'Data/' . $project_id . '/';
            if (is_dir($directory_path)) {
                $file = $directory_path . $model_id . '.model';
                $content = file_get_contents($file);
                echo $content;
            } else {
                echo '0';
            }
        } else {
            echo '0';
        }
    }
}
