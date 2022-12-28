GlobalVars = {
	"DATA_FOLDER_PATH": "./",
	"IM_FOLDER_NAME": "images",                 # IM stands for IMAGE
	"BB_FOLDER_NAME": "bounding_box",           # BB stands for BOUNDING BOXES
	"IS_FOLDER_NAME": "instance_segmentation"   # IS stands for INSTANCE SEGMENTATION
}
GlobalVars["IM_FOLDER_PATH"] = GlobalVars["DATA_FOLDER_PATH"] + GlobalVars["IM_FOLDER_NAME"]
GlobalVars["BB_FOLDER_PATH"] = GlobalVars["DATA_FOLDER_PATH"] + GlobalVars["BB_FOLDER_NAME"]
GlobalVars["IS_FOLDER_PATH"] = GlobalVars["DATA_FOLDER_PATH"] + GlobalVars["IS_FOLDER_NAME"]
