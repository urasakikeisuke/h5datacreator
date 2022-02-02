# -*- coding: utf-8 -*-

from typing import Dict
import numpy as np

TYPE_FLOAT16:str = 'float16'
TYPE_FLOAT32:str = 'float32'
TYPE_FLOAT64:str = 'float64'
TYPE_UINT8:str = 'uint8'
TYPE_INT8:str = 'int8'
TYPE_INT16:str = 'int16'
TYPE_INT32:str = 'int32'
TYPE_INT64:str = 'int64'
TYPE_MONO8:str = 'mono8'
TYPE_MONO16:str = 'mono16'
TYPE_BGR8:str = 'bgr8'
TYPE_RGB8:str = 'rgb8'
TYPE_BGRA8:str = 'bgra8'
TYPE_RGBA8:str = 'rgba8'
TYPE_DEPTH:str = 'depth'
TYPE_DISPARITY:str = 'disparity'
TYPE_POINTS:str = 'points'
TYPE_VOXEL_POINTS:str = 'voxel-points'
TYPE_SEMANTIC1D:str = 'semantic1d'
TYPE_SEMANTIC2D:str = 'semantic2d'
TYPE_SEMANTIC3D:str = 'semantic3d'
TYPE_VOXEL_SEMANTIC3D:str = 'voxel-semantic3d'
TYPE_POSE:str = 'pose'
TYPE_TRANSLATION:str = 'translation'
TYPE_QUATERNION:str = 'quaternion'
TYPE_INTRINSIC:str = 'intrinsic'
TYPE_COLOR:str = 'color'

SUBTYPE_TRANSLATION:str = 'translation'
SUBTYPE_ROTATION:str = 'rotation'
SUBTYPE_POINTS:str = 'points'
SUBTYPE_SEMANTIC1D:str = 'semantic1d'
SUBTYPE_FX:str = 'Fx'
SUBTYPE_FY:str = 'Fy'
SUBTYPE_CX:str = 'Cx'
SUBTYPE_CY:str = 'Cy'
SUBTYPE_HEIGHT:str = 'height'
SUBTYPE_WIDTH:str = 'width'
SUBTYPE_NAME:str = 'name'
SUBTYPE_VOXEL_POINTS:str = 'points-voxel'
SUBTYPE_VOXEL_SEMANTIC3D:str = 'semantic3d-voxel'

CONFIG_TAG_MINIBATCH:str = 'mini-batch'
CONFIG_TAG_TYPE:str = 'type'
CONFIG_TAG_FROM:str = 'from'
CONFIG_TAG_SHAPE:str = 'shape'
CONFIG_TAG_NORMALIZE:str = 'normalize'
CONFIG_TAG_RANGE:str = 'range'
CONFIG_TAG_KEY:str = 'key'
CONFIG_TAG_TF:str = 'tf'
CONFIG_TAG_TREE:str = 'tree'
CONFIG_TAG_LIST:str = 'list'
CONFIG_TAG_DATA:str = 'data'
CONFIG_TAG_FRAMEID:str = 'frame-id'
CONFIG_TAG_CHILDFRAMEID:str = 'child-frame-id'
CONFIG_TAG_CREATEFUNC:str = 'create-func'
CONFIG_TAG_SRCDATA:str = 'src-data'
CONFIG_TAG_TAG:str = 'tag'
CONFIG_TAG_LABEL:str = 'label'
CONFIG_TAG_CLASS:str = 'class'
CONFIG_TAG_SRC:str = 'src'
CONFIG_TAG_DST:str = 'dst'
CONFIG_TAG_CONFIG:str = 'config'
CONFIG_TAG_CONVERT:str = 'convert'
CONFIG_TAG_COLOR:str = 'color'
CONFIG_TAG_LABELTAG:str = 'label-tag'

H5_KEY_HEADER:str = 'header'
H5_KEY_LENGTH:str = 'length'
H5_KEY_LABEL:str = 'label'
H5_KEY_DATA:str = 'data'
H5_KEY_NAME:str = 'name'
H5_ATTR_TYPE:str = 'type'
H5_ATTR_STAMPSEC:str = 'stamp.sec'
H5_ATTR_STAMPNSEC:str = 'stamp.nsec'
H5_ATTR_FRAMEID:str = 'frame_id'
H5_ATTR_CHILDFRAMEID:str = 'child_frame_id'
H5_ATTR_BASELINE:str = 'base_line'
H5_ATTR_ARRAY:str = 'array'
H5_ATTR_FILEPATH:str = 'file_path'
H5_ATTR_MAPID:str = 'map_id'
H5_ATTR_LABELTAG:str = 'label_tag'
H5_ATTR_VOXELSIZE:str = 'voxel_size'
H5_ATTR_VOXELMIN:str = 'voxel_min'
H5_ATTR_VOXELMAX:str = 'voxel_max'
H5_ATTR_VOXELCENTER:str = 'voxel_center'
H5_ATTR_VOXELORIGIN:str = 'voxel_origin'

DTYPE_NUMPY:Dict[str, np.dtype] = {
    TYPE_FLOAT16: np.float16,
    TYPE_FLOAT32: np.float32,
    TYPE_FLOAT64: np.float64,
    TYPE_UINT8: np.uint8,
    TYPE_INT8: np.int8,
    TYPE_INT16: np.int16,
    TYPE_INT32: np.int32,
    TYPE_INT64: np.int64,
    TYPE_MONO8: np.uint8,
    TYPE_MONO16: np.uint16,
    TYPE_BGR8: np.uint8,
    TYPE_RGB8: np.uint8,
    TYPE_BGRA8: np.uint8,
    TYPE_RGBA8: np.uint8,
    TYPE_DEPTH: np.float32,
    TYPE_DISPARITY: np.float32,
    TYPE_POINTS: np.float32,
    TYPE_VOXEL_POINTS: np.object,
    SUBTYPE_VOXEL_POINTS: np.dtype([('x', np.float32), ('y', np.float32), ('z',np.float32)]),
    TYPE_SEMANTIC1D: np.uint8,
    TYPE_SEMANTIC2D: np.uint8,
    TYPE_SEMANTIC3D: None,
    TYPE_VOXEL_SEMANTIC3D: np.object,
    SUBTYPE_VOXEL_SEMANTIC3D: np.dtype([('x', np.float32), ('y', np.float32), ('z',np.float32), ('label',np.uint8)]),
    TYPE_POSE: None,
    TYPE_TRANSLATION: np.float32,
    TYPE_QUATERNION: np.float32,
    TYPE_INTRINSIC: np.float32,
    TYPE_COLOR: np.uint8,
}
