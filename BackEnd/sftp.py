import os
import pysftp


def download_csv_files_from_server():
    # downloads the files from the remote server into the local path.
    conn_options = pysftp.CnOpts()
    conn_options.hostkeys = None  # To disable host key checking.
    with pysftp.Connection('185.164.16.144', username='talm', password='malchital1', cnopts=conn_options) as sftp:
        sftp.cwd('/var/tmp/csv_files/')  # Transposing typed commands at sftp to pysftp.
        directory_attribute_list = sftp.listdir_attr()  # Returns sorted files list by SFTPAttribute.filename.
        for attr in directory_attribute_list:
            file_name = attr.filename
            remote_file_path = '/var/tmp/csv_files/' + file_name
            local_file_path = os.path.join(os.getcwd(), 'csv_files', file_name)
            #local_file_path = os.path.join('C:\\Users\\Desktop\DevOps\\CICD-ssh work\\flaskProject\\CsvFiles', file_name)
            local_file_path = 'C:\\Users\\Tal\\Desktop\\DevOps\\CICD-ssh work\\flaskProject\\CsvFiles\\' + file_name
            sftp.get(remote_file_path, local_file_path)


if __name__ == '__main__':
    download_csv_files_from_server()