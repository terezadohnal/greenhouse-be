################################################
## Přepis zedo-rpc pro python (nekompletní)
## Author: David Michalica Team 1, Matěj Prášil Team 2
## Documentation: https://bitbucket.org/dakel/node-zedo-rpc/src/master/API.md
## Date: 29.04.2024 MP v0.2
#################################################

import socket
import json
import os

class ZedoRPC: 
    def __init__(self, ip="127.0.0.1", port=40999):
        self.IP_ADDR = ip
        self.PORT = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def Connect(self):
        self.client_socket.connect((self.IP_ADDR, self.PORT))
        
    def Disconnect(self):
        self.client_socket.close()
        
    def Is_connected(self):
        try:
            remote_address = self.client_socket.getpeername()
            return True
        except OSError:
            return False

    def Call(self, method, params = {}, id = 1, buffer_size=4096):
        response_string = ""
        
        call_values = {
            'jsonrpc': '2.0', 
            'method': method, 
            'id': id,
            'params': params
        }
        
        json_string = json.dumps(call_values)
        bytes_to_send = json_string.encode('utf-8')    
        self.client_socket.send(bytes_to_send)
        
        while True:
            response = self.client_socket.recv(buffer_size)
            if not response:
                break
            response_string += response.decode('utf-8')

        return response_string

    def Generate_rec_folder_name(self):
        params = {
            'jsonrpc': '2.0', 
            'prefix': "wtf",
            'use_date': True,
            'use_hm': True,
            'use_sec': False,
            'name_delimiter': '-',
            'date_delimiter': '-',
            'time_delimiter': '-',
            'now': None
        }
        return self.Call("generate_rec_folder_name", params)

    def Compare_versions(self):
        return self.Call("Compare_versions")

    def Assert_min_version(self):
        return self.Call("Assert_min_version")

    def Copy_json(self):
        return self.Call("Copy_json")

    def Print_json(self):
        return self.Call("Print_json")

    def Is_json_object(self):
        return self.Call("Is_json_object")

    def Merge_json(self):
        return self.Call("Merge_json")

    def Is_zdat_directory(self, path):
        ret = False
        try:
            if os.path.isdir(path):
                zdat_path = os.path.join(path, "zedodata.zdat")
                if os.path.exists(zdat_path):
                    ret = os.path.isfile(zdat_path)
        except FileNotFoundError:
            ret = False
        return ret

    def GetSensors(self, verbosity):
        return self.Call("GetSensors", {'verbosity': verbosity} if verbosity else {})

    def GetSystemStatus(self):
        return self.Call("GetSystemStatus")

    def GetSystemTime(self):
        return self.Call("GetSystemTime")

    def GetConfiguration(self, verbosity):
        return self.Call("GetConfiguration", {'verbosity': verbosity} if verbosity else {})

    def Configure(self, config, verbosity):
        # Převedení konfigurace na pole, pokud není pole
        is_list = isinstance(config, list)
        items = config if is_list else [config]

        for item in items:
            if 'type' not in item:
                item['type'] = 'bunit'
        
        return self.call("Configure", {"items": items, "verbosity": verbosity})

    def ClearLiveData(self):
        return self.Call("ClearLiveData")

    def StartRecording(self, measurement_name, record_history_secs = 0):
        return self.Call("StartRecording", {
            "measurement_name": measurement_name, 
            "record_history_secs": record_history_secs
            })

    def PauseRecording(self):
        return self.Call("PauseRecording")

    def StopRecording(self):
        return self.Call("StopRecording")

    def GetRecordingState(self):
        return self.Call("GetRecordingState")

    def GetAppInfo(self):
        return self.Call("GetAppInfo")

    def GetActivePulsers(self):
        return self.Call("GetActivePulsers")

    def AllPulsersOff(self):
        return self.Call("AllPulsersOff")

    def pulser_configs_same(self):
        return self.Call("pulser_configs_same")

    def SetPulser(self):
        return self.Call("SetPulser")

    def EnableContinuousRecording(self):
        return self.Call("EnableContinuousRecording")

    def OpenFileReaderByPath(self, path):
        return self.Call("OpenFileReaderByPath", {'paths': path})

    def OpenFileReaderByName(self, name = ""):
        return self.Call('OpenFileReaderByName', {'name': name})

    def SetFileReaderPath(self, reader_id, path, update_name = False):
        return self.Call("SetFileReaderPath", {
            "reader_id": reader_id,
            "paths": path,
            "update_name": update_name
            })

    def GetFileReaderInfo(self, reader_id):
        return self.Call("GetFileReaderInfo", { "reader_id": reader_id})

    def GetFileReaderData(self, readerId):
        return self.Call("GetFileReaderData", { 'reader_id': readerId})

    def ExportFileReaderData(self, reader_id, outdir, subdir, export_cfg, make_unique_dir = True):
        return self.Call("ExportFileReaderData", {
            "path": outdir,
            "subdir": subdir,
            "unique_subdir": make_unique_dir,
            "reader_id": reader_id,
            "export_cfg": export_cfg
            })

    def ExportItems(self, items, outdir, subdir, export_cfg, make_unique_dir = True):
        return self.Call("ExportItems", {
            "path": outdir,
            "subdir": subdir,
            "unique_subdir": make_unique_dir,
            "items": items,
            "export_cfg": export_cfg
            }) 

    def CaptureGraphPictures(self, outdir, subdir = "graphs", make_unique_dir = True, make_unique_files = True):
        return self.Call("CaptureGraphPictures", {
            "path": outdir,
            "subdir": subdir,
            "unique_subdir": make_unique_dir,
            "unique_files": make_unique_files
            })

    def WaitFileReaderScanned(self, reader_id):
        return self.Call("WaitFileReaderScanned", { 'reader_id': reader_id})

    def WaitItemsIdle(self):
        return self.Call("WaitItemsIdle")

    def GetExportJobStatus(self, job_id):
        return self.Call("GetExportJobStatus", { "job_id": job_id })

    def AbortExportJob(self, job_id):
        return self.Call("AbortExportJob", { "job_id": job_id })

    def WaitBackroundJobFinished(self, job_id, timeout_seconds):
        return self.Call("WaitBackroundJobFinished", { "job_id": job_id, "timeout": timeout_seconds })

    def ExportJobProgressMonitor(self):
        return self.Call("ExportJobProgressMonitor")

    def GetItemInfo(self):
        return self.Call("GetItemInfo")

    def GetSubItems(self):
        return self.Call("GetSubItems")

# Příklad použití třídy
if __name__ == "__main__":
    print("# Přepis zedo-rpc pro python (nekompletní)\n# Author: David Michalica Team 1, Matěj Prášil Team 2\n# Documentation: https://bitbucket.org/dakel/node-zedo-rpc/src/master/API.md\n# Date: 29.04.2024 MP v0.2")
    
