provider "aws" {
     region = "us-east-1"
     shared_credentials_files = ["~/.aws/credentials"]
}

data "archive_file" "misc_code_zip" {
  type        = "zip"
  source_dir  = "./Misc"  # Relative path to your /misc directory
  output_path = "${path.module}/misc_code.zip"
}

data "archive_file" "google_trends_code_zip" {
  type        = "zip"
  source_dir  = "./googleTrendsDestination/"  # Relative path to your /googleTrendsDestination directory
  output_path = "${path.module}/google_trends_code.zip"
}

resource "aws_s3_bucket_object" "misc_code_zip" {
  bucket = "googlemlbucket"  # Replace with your S3 bucket name
  key    = "misc_code.zip"  # Desired object key within the bucket
  source = data.archive_file.misc_code_zip.output_path
}

resource "aws_s3_bucket_object" "google_trends_code_zip" {
  bucket = "googlemlbucket"  # Replace with your S3 bucket name
  key    = "google_trends_code.zip"  # Desired object key within the bucket
  source = data.archive_file.google_trends_code_zip.output_path
}

resource "aws_lambda_function" "my_lambda_function" {
  function_name    = "google_trends_webscrape"
  role             = "arn:aws:iam::833405552214:role/lambda_role"
  handler          = "index.handler"  # Specify the appropriate handler for your code
  runtime          = "python3.8"     # Specify the appropriate runtime for your code
  filename         = aws_s3_bucket_object.misc_code_zip.source  # Use the path to your zip file
  source_code_hash = filebase64sha256(data.archive_file.misc_code_zip.output_path)
}
