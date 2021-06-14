# -*- coding: utf-8 -*-

from typing import Union
import os
import h5py
import numpy as np

from .structure import *

class H5Dataset():
    """H5Dataset

    Class for creating an H5Dataset

    Args:
        path (str): path of H5Dataset
    """

    def __init__(self, path:str, mode='w') -> None:
        """__init__

        Args:
            path (str): path of H5Dataset
            mode (str): File mode ['w', 'a']
        """
        fullpath = os.path.abspath(path)

        if os.path.isdir(os.path.dirname(fullpath)) is False:
            raise NotADirectoryError('Directory "{0}" not found.'.format(os.path.dirname(fullpath)))

        if mode not in ['w', 'a']:
            raise ValueError('"mode" must be "w" or "a".')

        self.__h5file = h5py.File(fullpath, mode=mode)

        self.__h5file.create_group(H5_KEY_DATA)
        self.__current_index = -1

    def close(self) -> None:
        """close

        Close H5Dataset. Be sure to do this on exit.
        """
        h5_header:h5py.Group = self.__h5file.create_group(H5_KEY_HEADER)
        h5_header.create_dataset(H5_KEY_LENGTH, data=self.get_maximum_data_index()+1)

        self.__h5file.close()
        self.__current_index = -1
        self.__h5file = None

    def get_maximum_data_index(self) -> int:
        """get_maximum_data_index

        Get the maximum value of the index in '/data'.

        Returns:
            int: the maximum value of the index in '/data'.
        """
        h5_data:h5py.Group = self.__h5file[H5_KEY_DATA]
        h5_data_keys = np.array([int(key) for key in h5_data.keys()])
        h5_data_max_index = np.max(h5_data_keys)
        return h5_data_max_index

    def get_current_data_group(self) -> h5py.Group:
        """get_current_data_group

        Get the group of indexes in '/data' to be edited.

        Returns:
            h5py.Group: the group of indexes in '/data' to be edited.
        """
        h5_data:h5py.Group = self.__h5file[H5_KEY_DATA]
        if self.__current_index < 0:
            self.__current_index = 0
            data_group = h5_data.create_group(str(self.__current_index))
        else:
            data_group = h5_data[str(self.__current_index)]
        return data_group

    def get_current_data_index(self) -> int:
        """get_current_data_index

        Get the index in '/data' to be edited.

        Returns:
            int: the index in '/data' to be edited.
        """
        return self.__current_index

    def get_next_data_group(self) -> h5py.Group:
        """get_next_data_group

        Get the next group of index in '/data'.

        Returns:
            h5py.Group: the next group of index in '/data'.
        """
        self.__current_index += 1
        h5_data:h5py.Group = self.__h5file[H5_KEY_DATA]
        data_group = h5_data.get(str(self.__current_index))
        if data_group is None:
            data_group = h5_data.create_group(str(self.__current_index))
        return data_group

    def get_data_group_from_index(self, index:int) -> h5py.Group:
        """get_data_group_from_index

        Get the group at the specified index in '/data'.

        Args:
            index (int): index in '/data'.

        Raises:
            ValueError: if 'index' is out of range.

        Returns:
            h5py.Group: the group at the specified index in '/data'.
        """
        max_index = self.get_maximum_data_index()
        if index < 0 or max_index < index:
            raise ValueError('Out of range.')
        self.__current_index = index
        return self.__h5file[H5_KEY_DATA + '/' + str(index)]

    def get_label_group(self, tag:str) -> h5py.Group:
        """get_label_group

        Get the group of '/label/[tag]'.

        Args:
            tag (str): tag for label settings

        Raises:
            NameError: if "len(tag)" less than 1.

        Returns:
            h5py.Group: the group of '/label/[tag]'
        """
        if len(tag) < 1:
            raise NameError('"len(tag)" must be greater than 0.')
        h5_label:h5py.Group = self.__h5file.get(H5_KEY_LABEL)
        if h5_label is None:
            h5_label = self.__h5file.create_group(H5_KEY_LABEL)
        h5_label_tag:h5py.Group = h5_label.get(tag)
        if h5_label_tag is None:
            h5_label_tag = h5_label.create_group(tag)
        return h5_label_tag

    def get_common_group(self, tag:str) -> h5py.Group:
        """get_common_group

        Get a group of common data '/[tag]' independent of the index.

        Args:
            tag (str): tag for a group of common data

        Raises:
            NameError: if 'tag' is reserved name.

        Returns:
            h5py.Group: a group of common data '/[tag]'
        """
        if {tag} <= {H5_KEY_HEADER, H5_KEY_DATA, H5_KEY_LABEL}:
            raise NameError('"{}" is reserved.'.format(tag))
        h5_common:h5py.Group = self.__h5file.get(tag)
        if h5_common is None:
            h5_common = self.__h5file.create_group(tag)
        return h5_common

def set_uint8(h5_group:Union[h5py.Group, h5py.File], tag:str, data:int, stamp_sec:int=0, stamp_nsec:int=0) -> None:
    """set_uint8

    'uint8'型のデータを格納する

    Args:
        h5_group (h5py.Group | h5py.File): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (int): 整数型のデータ
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.
    """
    h5_data:h5py.Dataset = h5_group.create_dataset(tag, data=data, dtype=np.uint8)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_UINT8
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec

def set_int8(h5_group:Union[h5py.Group, h5py.File], tag:str, data:int, stamp_sec:int=0, stamp_nsec:int=0) -> None:
    """set_int8

    'int8'型のデータを格納する

    Args:
        h5_group (h5py.Group | h5py.File): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (int): 整数型のデータ
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.
    """
    h5_data:h5py.Dataset = h5_group.create_dataset(tag, data=data, dtype=np.int8)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_INT8
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec

def set_int16(h5_group:Union[h5py.Group, h5py.File], tag:str, data:int, stamp_sec:int=0, stamp_nsec:int=0) -> None:
    """set_int16

    'int16'型のデータを格納する

    Args:
        h5_group (h5py.Group | h5py.File): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (int): 整数型のデータ
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.
    """
    h5_data:h5py.Dataset = h5_group.create_dataset(tag, data=data, dtype=np.int16)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_INT16
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec

def set_int32(h5_group:Union[h5py.Group, h5py.File], tag:str, data:int, stamp_sec:int=0, stamp_nsec:int=0) -> None:
    """set_int32

    'int32'型のデータを格納する

    Args:
        h5_group (h5py.Group | h5py.File): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (int): 整数型のデータ
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.
    """
    h5_data:h5py.Dataset = h5_group.create_dataset(tag, data=data, dtype=np.int32)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_INT32
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec

def set_int64(h5_group:Union[h5py.Group, h5py.File], tag:str, data:int, stamp_sec:int=0, stamp_nsec:int=0) -> None:
    """set_int64

    'int64'型のデータを格納する

    Args:
        h5_group (h5py.Group | h5py.File): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (int): 整数型のデータ
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.
    """
    h5_data:h5py.Dataset = h5_group.create_dataset(tag, data=data, dtype=np.int64)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_INT64
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec

def set_float16(h5_group:Union[h5py.Group, h5py.File], tag:str, data:float, stamp_sec:int=0, stamp_nsec:int=0) -> None:
    """set_float16

    'float16'型のデータを格納する

    Args:
        h5_group (h5py.Group | h5py.File): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (float): 浮動小数点型のデータ
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.
    """
    h5_data:h5py.Dataset = h5_group.create_dataset(tag, data=data, dtype=np.float16)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_FLOAT16
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec

def set_float32(h5_group:Union[h5py.Group, h5py.File], tag:str, data:float, stamp_sec:int=0, stamp_nsec:int=0) -> None:
    """set_float32

    'float32'型のデータを格納する

    Args:
        h5_group (h5py.Group | h5py.File): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (float): 浮動小数点型のデータ
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.
    """
    h5_data:h5py.Dataset = h5_group.create_dataset(tag, data=data, dtype=np.float32)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_FLOAT32
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec

def set_float64(h5_group:Union[h5py.Group, h5py.File], tag:str, data:float, stamp_sec:int=0, stamp_nsec:int=0) -> None:
    """set_float64

    'float64'型のデータを格納する

    Args:
        h5_group (h5py.Group | h5py.File): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (float): 浮動小数点型のデータ
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.
    """
    h5_data:h5py.Dataset = h5_group.create_dataset(tag, data=data, dtype=np.float64)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_FLOAT64
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec

def set_mono8(h5_group:Union[h5py.Group, h5py.File], tag:str, data:np.ndarray, frame_id:str, stamp_sec:int=0, stamp_nsec:int=0) -> None:
    """set_mono8

    'mono8'型の画像データを格納する

    Args:
        h5_group (h5py.Group | h5py.File): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (np.ndarray): shape=(H, W), dtype=np.uint8 の画像データ
        frame_id (str): 座標系
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.

    Raises:
        ValueError: if \"data.shape\" is not (H, W).
        TypeError: if \"data.dtype\" is not \"np.uint8\".
    """
    if len(data.shape) != 2:
        raise ValueError('"data.shape" must be (H, W).')
    dtype:np.dtype = DTYPE_NUMPY[TYPE_MONO8]
    if data.dtype != dtype:
        raise TypeError('"data.dtype" must be "{}".'.format(str(dtype)))
    h5_data:h5py.Dataset = h5_group.create_dataset(tag, data=data)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_MONO8
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec
    h5_data.attrs[H5_ATTR_FRAMEID] = frame_id

def set_mono16(h5_group:Union[h5py.Group, h5py.File], tag:str, data:np.ndarray, frame_id:str, stamp_sec:int=0, stamp_nsec:int=0) -> None:
    """set_mono16

    'mono16'型の画像データを格納する

    Args:
        h5_group (h5py.Group | h5py.File): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (np.ndarray): shape=(H, W), dtype=np.uint16 の画像データ
        frame_id (str): 座標系
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.

    Raises:
        ValueError: if \"data.shape\" is not (H, W).
        TypeError: if \"data.dtype\" is not \"np.uint16\".
    """
    if len(data.shape) != 2:
        raise ValueError('"data.shape" must be (H, W).')
    dtype:np.dtype = DTYPE_NUMPY[TYPE_MONO16]
    if data.dtype != dtype:
        raise TypeError('"data.dtype" must be "{}".'.format(str(dtype)))
    h5_data:h5py.Dataset = h5_group.create_dataset(tag, data=data)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_MONO16
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec
    h5_data.attrs[H5_ATTR_FRAMEID] = frame_id

def set_bgr8(h5_group:Union[h5py.Group, h5py.File], tag:str, data:np.ndarray, frame_id:str, stamp_sec:int=0, stamp_nsec:int=0) -> None:
    """set_bgr8

    'bgr8'型の画像データを格納する

    Args:
        h5_group (h5py.Group | h5py.File): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (np.ndarray): shape=(H, W, 3), dtype=np.uint8 の画像データ
        frame_id (str): 座標系
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.

    Raises:
        ValueError: if \"data.shape\" is not (H, W, 3).
        TypeError: if \"data.dtype\" is not \"np.uint8\".
    """
    if len(data.shape) != 3:
        raise ValueError('"data.shape" must be (H, W, 3).')
    if data.shape[2] != 3:
        raise ValueError('"data.shape" must be (H, W, 3).')
    dtype:np.dtype = DTYPE_NUMPY[TYPE_BGR8]
    if data.dtype != dtype:
        raise TypeError('"data.dtype" must be "{}".'.format(str(dtype)))
    h5_data:h5py.Dataset = h5_group.create_dataset(tag, data=data)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_BGR8
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec
    h5_data.attrs[H5_ATTR_FRAMEID] = frame_id

def set_rgb8(h5_group:Union[h5py.Group, h5py.File], tag:str, data:np.ndarray, frame_id:str, stamp_sec:int=0, stamp_nsec:int=0) -> None:
    """set_rgb8

    'rgb8'型の画像データを格納する

    Args:
        h5_group (h5py.Group | h5py.File): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (np.ndarray): shape=(H, W, 3), dtype=np.uint8 の画像データ
        frame_id (str): 座標系
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.

    Raises:
        ValueError: if \"data.shape\" is not (H, W, 3).
        TypeError: if \"data.dtype\" is not \"np.uint8\".
    """
    if len(data.shape) != 3:
        raise ValueError('"data.shape" must be (H, W, 3).')
    if data.shape[2] != 3:
        raise ValueError('"data.shape" must be (H, W, 3).')
    dtype:np.dtype = DTYPE_NUMPY[TYPE_RGB8]
    if data.dtype != dtype:
        raise TypeError('"data.dtype" must be "{}".'.format(str(dtype)))
    h5_data:h5py.Dataset = h5_group.create_dataset(tag, data=data)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_RGB8
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec
    h5_data.attrs[H5_ATTR_FRAMEID] = frame_id

def set_bgra8(h5_group:Union[h5py.Group, h5py.File], tag:str, data:np.ndarray, frame_id:str, stamp_sec:int=0, stamp_nsec:int=0) -> None:
    """set_bgra8

    'bgra8'型の画像データを格納する

    Args:
        h5_group (h5py.Group | h5py.File): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (np.ndarray): shape=(H, W, 4), dtype=np.uint8 の画像データ
        frame_id (str): 座標系
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.

    Raises:
        ValueError: if \"data.shape\" is not (H, W, 4).
        TypeError: if \"data.dtype\" is not \"np.uint8\".
    """
    if len(data.shape) != 3:
        raise ValueError('"data.shape" must be (H, W, 4).')
    if data.shape[2] != 4:
        raise ValueError('"data.shape" must be (H, W, 4).')
    dtype:np.dtype = DTYPE_NUMPY[TYPE_BGRA8]
    if data.dtype != dtype:
        raise TypeError('"data.dtype" must be "{}".'.format(str(dtype)))
    h5_data:h5py.Dataset = h5_group.create_dataset(tag, data=data)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_BGRA8
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec
    h5_data.attrs[H5_ATTR_FRAMEID] = frame_id

def set_rgba8(h5_group:Union[h5py.Group, h5py.File], tag:str, data:np.ndarray, frame_id:str, stamp_sec:int=0, stamp_nsec:int=0) -> None:
    """set_rgba8

    'rgba8'型の画像データを格納する

    Args:
        h5_group (h5py.Group | h5py.File): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (np.ndarray): shape=(H, W, 4), dtype=np.uint8 の画像データ
        frame_id (str): 座標系
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.

    Raises:
        ValueError: if \"data.shape\" is not (H, W, 4).
        TypeError: if \"data.dtype\" is not \"np.uint8\".
    """
    if len(data.shape) != 3:
        raise ValueError('"data.shape" must be (H, W, 4).')
    if data.shape[2] != 4:
        raise ValueError('"data.shape" must be (H, W, 4).')
    dtype:np.dtype = DTYPE_NUMPY[TYPE_RGBA8]
    if data.dtype != dtype:
        raise TypeError('"data.dtype" must be "{}".'.format(str(dtype)))
    h5_data:h5py.Dataset = h5_group.create_dataset(tag, data=data)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_RGBA8
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec
    h5_data.attrs[H5_ATTR_FRAMEID] = frame_id

def set_depth(h5_group:Union[h5py.Group, h5py.File], tag:str, data:np.ndarray, frame_id:str, stamp_sec:int=0, stamp_nsec:int=0) -> None:
    """set_depth

    'depth'型の画像データを格納する

    Args:
        h5_group (h5py.Group | h5py.File): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (np.ndarray): shape=(H, W), dtype=np.float32 の画像データ
        frame_id (str): 座標系
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.

    Raises:
        ValueError: if \"data.shape\" is not (H, W).
        TypeError: if \"data.dtype\" is not \"np.float32\".
    """
    if len(data.shape) != 2:
        raise ValueError('"data.shape" must be (H, W).')
    dtype:np.dtype = DTYPE_NUMPY[TYPE_DEPTH]
    if data.dtype != dtype:
        raise TypeError('"data.dtype" must be "{}".'.format(str(dtype)))
    h5_data:h5py.Dataset = h5_group.create_dataset(tag, data=data)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_DEPTH
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec
    h5_data.attrs[H5_ATTR_FRAMEID] = frame_id

def set_points(h5_group:Union[h5py.Group, h5py.File], tag:str, data:np.ndarray, frame_id:str, stamp_sec:int=0, stamp_nsec:int=0, map_id:str=None) -> None:
    """set_points

    'points'型の点群データを格納する

    Args:
        h5_group (h5py.Group | h5py.File): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (np.ndarray): shape=(N, 3), dtype=np.float32 の点群データ
        frame_id (str): 座標系
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.
        map_id (str, optional): 三次元点群地図のID. 三次元点群地図として使用する場合は必須. Defaults to None.

    Raises:
        ValueError: if \"data.shape\" is not (N, 3).
        TypeError: if \"data.dtype\" is not \"np.float32\".
    """
    if len(data.shape) != 2:
        raise ValueError('"data.shape" must be (N, 3).')
    if data.shape[1] != 3:
        raise ValueError('"data.shape" must be (N, 3).')
    dtype:np.dtype = DTYPE_NUMPY[TYPE_POINTS]
    if data.dtype != dtype:
        raise TypeError('"data.dtype" must be "{}".'.format(str(dtype)))
    h5_data:h5py.Dataset = h5_group.create_dataset(tag, data=data)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_POINTS
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec
    h5_data.attrs[H5_ATTR_FRAMEID] = frame_id
    if map_id is not None:
        h5_data.attrs[H5_ATTR_MAPID] = map_id

def set_voxel_points(h5group:Union[h5py.Group, h5py.File], tag:str, data:np.ndarray,
    frame_id:str, voxel_size:float, voxels_min:Tuple[float, float, float],
    voxels_max:Tuple[float, float, float], voxels_center:Tuple[float, float, float],
    voxels_origin:Tuple[int, int, int], label_tag:str=None, stamp_sec:int=0, stamp_nsec:int=0, map_id:str=None) -> None:
    """set_voxel_points

    'voxel-points'型のデータを格納する

    Args:
        h5_group (Union[h5py.Group, h5py.File]): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (np.ndarray): VoxelGridMap (compound(N,)['x', 'y', 'z']を格納したNumpy(Z, Y, X)行列)
        frame_id (str): 座標系
        voxel_size (float): Voxelのサイズ[m]
        voxels_min (Tuple[float, float, float]): VoxelGridMapの範囲の最小値(z_min, y_min, x_min)
        voxels_max (Tuple[float, float, float]): VoxelGridMapの範囲の最大値(z_max, y_max, x_max)
        voxels_center (Tuple[float, float, float]): VoxelGridMapの中心座標(z_center, y_center, x_center)
        voxels_origin (Tuple[int, int, int]): VoxelGridMapの中心のVoxelのインデックス(z_origin, y_origin, x_origin)
        label_tag (str): 依存するラベルのタグ
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.
        map_id (str, optional): 三次元点群地図のID. 三次元点群地図として使用する場合は必須. Defaults to None.
    """
    dtype:np.dtype = DTYPE_NUMPY[TYPE_VOXEL_POINTS]
    if data.dtype != dtype:
        raise TypeError('"data.dtype" must be "{}".'.format(str(dtype)))

    h5_data:h5py.Dataset = h5group.create_dataset(tag, data=data, dtype=h5py.special_dtype(vlen=DTYPE_NUMPY[SUBTYPE_VOXEL_POINTS]))
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_VOXEL_POINTS
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec
    h5_data.attrs[H5_ATTR_FRAMEID] = frame_id
    if label_tag is not None:
        h5_data.attrs[H5_ATTR_LABELTAG] = label_tag
    if map_id is not None:
        h5_data.attrs[H5_ATTR_MAPID] = map_id
    h5_data.attrs[H5_ATTR_VOXELSIZE] = voxel_size
    h5_data.attrs[H5_ATTR_VOXELMIN] = np.array(voxels_min)
    h5_data.attrs[H5_ATTR_VOXELMAX] = np.array(voxels_max)
    h5_data.attrs[H5_ATTR_VOXELCENTER] = np.array(voxels_center)
    h5_data.attrs[H5_ATTR_VOXELORIGIN] = np.array(voxels_origin)

def set_semantic1d(h5_group:Union[h5py.Group, h5py.File], tag:str, data:np.ndarray, label_tag:str, stamp_sec:int=0, stamp_nsec:int=0) -> None:
    """set_semantic1d

    'semantic1d'型の1次元のラベルデータを格納する

    Args:
        h5_group (h5py.Group | h5py.File): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (np.ndarray): shape=(N,), dtype=np.uint8 の1次元ラベルデータ
        label_tag (str): 依存するラベルのタグ
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.

    Raises:
        ValueError: if \"data.shape\" is not (N,).
        TypeError: if \"data.dtype\" is not \"np.uint8\".
    """
    if len(data.shape) != 1:
        raise ValueError('"data.shape" must be (N,).')
    dtype:np.dtype = DTYPE_NUMPY[TYPE_SEMANTIC1D]
    if data.dtype != dtype:
        raise TypeError('"data.dtype" must be "{}".'.format(str(dtype)))
    h5_data:h5py.Dataset = h5_group.create_dataset(tag, data=data)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_SEMANTIC1D
    h5_data.attrs[H5_ATTR_LABELTAG] = label_tag
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec

def set_semantic2d(h5_group:Union[h5py.Group, h5py.File], tag:str, data:np.ndarray, frame_id:str, label_tag:str, stamp_sec:int=0, stamp_nsec:int=0) -> None:
    """set_semantic2d

    'semantic2d'型のラベルデータを格納する

    Args:
        h5_group (h5py.Group | h5py.File): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (np.ndarray): shape=(H, W), dtype=np.uint8 の画像データ
        frame_id (str): 座標系
        label_tag (str): 依存するラベルのタグ
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.

    Raises:
        ValueError: if \"data.shape\" is not (H, W).
        TypeError: if \"data.dtype\" is not \"np.uint8\".
    """
    if len(data.shape) != 2:
        raise ValueError('"data.shape" must be (H, W).')
    dtype:np.dtype = DTYPE_NUMPY[TYPE_SEMANTIC2D]
    if data.dtype != dtype:
        raise TypeError('"data.dtype" must be "{}".'.format(str(dtype)))
    h5_data:h5py.Dataset = h5_group.create_dataset(tag, data=data)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_SEMANTIC2D
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec
    h5_data.attrs[H5_ATTR_FRAMEID] = frame_id
    h5_data.attrs[H5_ATTR_LABELTAG] = label_tag

def set_semantic3d(h5_group:Union[h5py.Group, h5py.File], tag:str, data_points:np.ndarray, data_semantic1d:np.ndarray, frame_id:str, label_tag:str, stamp_sec:int=0, stamp_nsec:int=0, map_id:str=None) -> None:
    """set_semantic3d

    'semantic3d'型のラベル付き点群データを格納する

    Args:
        h5_group (h5py.Group | h5py.File): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data_points (np.ndarray): shape=(N, 3), dtype=np.float32 のラベル付き点群を構成する点群データ
        data_semantic1d (np.ndarray): shape=(N,), dtype=np.uint8 のラベル付き点群を構成する1次元ラベルデータ
        frame_id (str): 座標系
        label_tag (str): 依存するラベルのタグ
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.
        map_id (str, optional): 三次元点群地図のID. 三次元点群地図として使用する場合は必須. Defaults to None.

    Raises:
        ValueError: if data_points.shape[0] != data_semantic1d.shape[0].
    """
    if data_points.shape[0] != data_semantic1d.shape[0]:
        raise ValueError('"data_points.shape[0] != data_semantic1d.shape[0]"')
    h5_data:h5py.Group = h5_group.create_group(tag)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_SEMANTIC3D
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec
    h5_data.attrs[H5_ATTR_FRAMEID] = frame_id
    h5_data.attrs[H5_ATTR_LABELTAG] = label_tag
    if map_id is not None:
        h5_data.attrs[H5_ATTR_MAPID] = map_id
    set_points(h5_data, SUBTYPE_POINTS, data_points, frame_id, stamp_sec, stamp_nsec, map_id)
    set_semantic1d(h5_data, SUBTYPE_SEMANTIC1D, data_semantic1d, label_tag, stamp_sec, stamp_nsec)

def set_voxel_semantic3d(h5group:Union[h5py.Group, h5py.File], tag:str, data:np.ndarray,
    frame_id:str, voxel_size:float, voxels_min:Tuple[float, float, float],
    voxels_max:Tuple[float, float, float], voxels_center:Tuple[float, float, float],
    voxels_origin:Tuple[int, int, int], label_tag:str=None, stamp_sec:int=0, stamp_nsec:int=0, map_id:str=None) -> None:
    """set_voxel_semantic3d

    'voxel-semantic3d'型のデータを格納する

    Args:
        h5_group (Union[h5py.Group, h5py.File]): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (np.ndarray): VoxelGridMap (compound(N,)['x', 'y', 'z', 'label']を格納したNumpy(Z, Y, X)行列)
        frame_id (str): 座標系
        voxel_size (float): Voxelのサイズ[m]
        voxels_min (Tuple[float, float, float]): VoxelGridMapの範囲の最小値(z_min, y_min, x_min)
        voxels_max (Tuple[float, float, float]): VoxelGridMapの範囲の最大値(z_max, y_max, x_max)
        voxels_center (Tuple[float, float, float]): VoxelGridMapの中心座標(z_center, y_center, x_center)
        voxels_origin (Tuple[int, int, int]): VoxelGridMapの中心のVoxelのインデックス(z_origin, y_origin, x_origin)
        label_tag (str): 依存するラベルのタグ
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.
        map_id (str, optional): 三次元点群地図のID. 三次元点群地図として使用する場合は必須. Defaults to None.
    """
    dtype:np.dtype = DTYPE_NUMPY[TYPE_VOXEL_SEMANTIC3D]
    if data.dtype != dtype:
        raise TypeError('"data.dtype" must be "{}".'.format(str(dtype)))

    h5_data:h5py.Dataset = h5group.create_dataset(tag, data=data, dtype=h5py.special_dtype(vlen=DTYPE_NUMPY[SUBTYPE_VOXEL_SEMANTIC3D]))
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_VOXEL_SEMANTIC3D
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec
    h5_data.attrs[H5_ATTR_FRAMEID] = frame_id
    if label_tag is not None:
        h5_data.attrs[H5_ATTR_LABELTAG] = label_tag
    if map_id is not None:
        h5_data.attrs[H5_ATTR_MAPID] = map_id
    h5_data.attrs[H5_ATTR_VOXELSIZE] = voxel_size
    h5_data.attrs[H5_ATTR_VOXELMIN] = np.array(voxels_min)
    h5_data.attrs[H5_ATTR_VOXELMAX] = np.array(voxels_max)
    h5_data.attrs[H5_ATTR_VOXELCENTER] = np.array(voxels_center)
    h5_data.attrs[H5_ATTR_VOXELORIGIN] = np.array(voxels_origin)

def set_pose(h5_group:Union[h5py.Group, h5py.File], tag:str, data_translation:np.ndarray, data_quaternion:np.ndarray, frame_id:str, child_frame_id:str, stamp_sec:int=0, stamp_nsec:int=0) -> None:
    """set_pose

    'pose'型のデータを格納する

    Args:
        h5_group (Union[h5py.Group, h5py.File]): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data_translation (np.ndarray): [tx, ty, tz], dtype=np.float32 or np.float64 の並進ベクトル
        data_quaternion (np.ndarray): [qx, qy, qz, qw], dtype=np.float32 or np.float64 のクォータニオン
        frame_id (str): 座標系
        child_frame_id (str): 子の座標系
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.
    """
    h5_data:h5py.Group = h5_group.create_group(tag)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_POSE
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec
    h5_data.attrs[H5_ATTR_FRAMEID] = frame_id
    h5_data.attrs[H5_ATTR_CHILDFRAMEID] = child_frame_id
    set_translation(h5_data, SUBTYPE_TRANSLATION, data_translation, stamp_sec, stamp_nsec)
    set_quaternion(h5_data, SUBTYPE_ROTATION, data_quaternion, stamp_sec, stamp_nsec)

def set_translation(h5_group:Union[h5py.Group, h5py.File], tag:str, data:np.ndarray, stamp_sec:int=0, stamp_nsec:int=0) -> None:
    """set_translation

    'translation'型のデータを格納する

    Args:
        h5_group (Union[h5py.Group, h5py.File]): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (np.ndarray): [tx, ty, tz], dtype=np.float32 or np.float64 の並進ベクトル
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.

    Raises:
        ValueError: if \"data\" is not [tx, ty, tz].
        TypeError: if \"data.dtype\" is not \"np.float32\" or \"np.float54\".
    """
    if len(data.shape) != 1:
        raise ValueError('"data" must be [tx, ty, tz].')
    if data.shape[0] != 3:
        raise ValueError('"data" must be [tx, ty, tz].')
    if {data.dtype} <= {np.float32, np.float64}:
        raise TypeError('"data.dtype" must be "np.float32" or "np.float64".')
    h5_data:h5py.Dataset = h5_group.create_dataset(tag, data=data)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_TRANSLATION
    h5_data.attrs[H5_ATTR_ARRAY] = "x,y,z"
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec

def set_quaternion(h5_group:Union[h5py.Group, h5py.File], tag:str, data:np.ndarray, stamp_sec:int=0, stamp_nsec:int=0) -> None:
    """set_quaternion

    'quaternion'型のデータを格納する

    Args:
        h5_group (Union[h5py.Group, h5py.File]): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data (np.ndarray): [qx, qy, qz, qw], dtype=np.float32 or np.float64 の並進ベクトル
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.

    Raises:
        ValueError: if \"data\" is not [qx, qy, qz, qw].
        TypeError: if \"data.dtype\" is not \"np.float32\" or \"np.float54\".
    """
    if len(data.shape) != 1:
        raise ValueError('"data" must be [qx, qy, qz, qw].')
    if data.shape[0] != 4:
        raise ValueError('"data" must be [qx, qy, qz, qw].')
    if {data.dtype} <= {np.float32, np.float64}:
        raise TypeError('"data.dtype" must be "np.float32" or "np.float64".')
    h5_data:h5py.Dataset = h5_group.create_dataset(tag, data=data)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_QUATERNION
    h5_data.attrs[H5_ATTR_ARRAY] = "x,y,z,w"
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec

def set_intrinsic(h5_group:Union[h5py.Group, h5py.File], tag:str, data_fx:float, data_fy:float, data_cx:float, data_cy:float, data_height:int, data_width:int, frame_id:str, stamp_sec:int=0, stamp_nsec:int=0) -> None:
    """set_intrinsic

    'intrinsic'型のデータを格納する

    Args:
        h5_group (Union[h5py.Group, h5py.File]): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data_fx (float): 焦点距離[px] (水平方向)
        data_fy (float): 焦点距離[px] (垂直方向)
        data_cx (float): 中心座標[px] (水平方向)
        data_cy (float): 中心座標[px] (垂直方向)
        data_height (int): 画像の縦幅[px]
        data_width (int): 画像の横幅[px]
        frame_id (str): 座標系
        stamp_sec (int, optional): タイムスタンプ(整数部[sec]). Defaults to 0.
        stamp_nsec (int, optional): タイムスタンプ(小数部[nsec]). Defaults to 0.
    """
    h5_data:h5py.Group = h5_group.create_group(tag)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_INTRINSIC
    h5_data.attrs[H5_ATTR_STAMPSEC] = stamp_sec
    h5_data.attrs[H5_ATTR_STAMPNSEC] = stamp_nsec
    h5_data.attrs[H5_ATTR_FRAMEID] = frame_id
    h5_data.create_dataset(SUBTYPE_FX, data=data_fx, dtype=np.float64)
    h5_data.create_dataset(SUBTYPE_FY, data=data_fy, dtype=np.float64)
    h5_data.create_dataset(SUBTYPE_CX, data=data_cx, dtype=np.float64)
    h5_data.create_dataset(SUBTYPE_CY, data=data_cy, dtype=np.float64)
    h5_data.create_dataset(SUBTYPE_HEIGHT, data=data_height, dtype=np.uint32)
    h5_data.create_dataset(SUBTYPE_WIDTH, data=data_width, dtype=np.uint32)

def set_color(h5_group:Union[h5py.Group, h5py.File], tag:str, data_r:int, data_g:int, data_b:int) -> None:
    """set_color

    'color'型のデータを格納する

    Args:
        h5_group (Union[h5py.Group, h5py.File]): 格納するH5Datasetのグループ
        tag (str): データのタグ
        data_r (int): 赤の画素値 [0-255]
        data_g (int): 緑の画素値 [0-255]
        data_b (int): 青の画素値 [0-255]
    """
    data:np.ndarray = np.array([data_b, data_g, data_r], dtype=np.uint8)
    h5_data:h5py.Dataset = h5_group.create_dataset(tag, data=data)
    h5_data.attrs[H5_ATTR_TYPE] = TYPE_COLOR
    h5_data.attrs[H5_ATTR_ARRAY] = "b,g,r"

def set_label_config(h5_group:Union[h5py.Group, h5py.File], index:int, name:str, data_r:int, data_g:int, data_b:int) -> None:
    """set_label_config

    ラベルの設定を格納する

    Args:
        h5_group (Union[h5py.Group, h5py.File]): 格納するH5Datasetのグループ
        index (int): ラベルのインデックス
        name (str): ラベルの名前
        data_r (int): 赤の画素値 [0-255]
        data_g (int): 緑の画素値 [0-255]
        data_b (int): 青の画素値 [0-255]
    """
    h5_label_index:h5py.Group = h5_group.create_group(str(index))
    h5_label_index.create_dataset(SUBTYPE_NAME, data=name)
    set_color(h5_label_index, TYPE_COLOR, data_r, data_g, data_b)
