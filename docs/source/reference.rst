=========
Reference
=========

クラス
======

H5Dataset
---------

.. code-block:: python

  from h5datacreator import H5Dataset
  h5file = H5Dataset(path='sample.hdf5')

データセットを格納するオブジェクト.

close
^^^^^

.. code-block:: python

  def close() -> None:

ファイルを閉じる. 閉じる前に必ず実行する. ``/data/`` 内にデータが存在しない場合, エラーとなる.

get_maximum_data_index
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  def get_maximum_data_index() -> int:

``/data/`` 内にある連続データのインデックスの最大値を取得する.
``/data/`` 内にデータが存在しない場合, エラーとなる.

* Returns:

  * ``int``: ``/data/`` 内にある連続データのインデックスの最大値

get_current_data_group
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  def get_current_data_group() -> h5py.Group:

``/data/`` 内の現在編集しているグループを取得する.
``/data`` が存在しない場合, ``/data/`` 内にグループが存在しない場合は, ``/data/0/`` グループを作成して返す.

* Returns:

  * ``h5py.Group``: ``/data/`` 内の現在編集しているグループ

get_current_data_index
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  def get_current_data_index() -> int:

``/data/`` 内の現在編集しているグループのインデックスを取得する.

* Returns:

  * ``int``: ``/data/`` 内の現在編集しているグループのインデックス

get_next_data_group
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  def get_next_data_group() -> h5py.Group:

``/data/`` 内の次のインデックスのグループを取得する.
``/data`` が存在しない場合, ``/data/`` 内にグループが存在しない場合は, ``/data/0/`` グループを作成して返す.

* Returns:

  * ``h5py.Group``: ``/data/`` 内の次のインデックスのグループ

get_data_group_from_index
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  def get_data_group_from_index(index: int) -> h5py.Group:

``/data/`` 内の指定したインデックスのグループを取得する.
``/data/`` 内に指定したインデックスのグループが存在しない場合, エラーとなる.

* Args:

  * ``index (int)``: ``/data/`` 内のグループのインデックス

* Returns:

  * ``h5py.Group``: ``/data/`` 内の指定したインデックスのグループ

get_label_group
^^^^^^^^^^^^^^^

.. code-block:: python

  def get_label_group(tag: str) -> h5py.Group:

ラベルセットのデータを格納するグループ ``/label/[tag]`` を取得する.

* Args:

  * ``tag (str)``: ラベルセットのタグ

* Returns:

  * ``h5py.Group``: ラベルセットのデータを格納するグループ

get_common_group
^^^^^^^^^^^^^^^^

.. code-block:: python

  def get_common_group(tag:str) -> h5py.Group:

非連続な共通データを格納するグループを取得する.

* Args:

  * ``tag (str)``: 共通データのタグ

* Returns:

  * ``h5py.Group``: 共通データを格納するグループ

関数
====

数値の格納
----------

set_uint8
^^^^^^^^^

.. code-block:: python

  def set_uint8(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data: int,
    stamp_sec: int=0,
    stamp_nsec: int=0
  ) -> None:

符号なし8bit整数型 ``uint8`` のデータを格納する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (int)``: データ
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

set_int8
^^^^^^^^

.. code-block:: python

  def set_int8(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data: int,
    stamp_sec: int=0,
    stamp_nsec: int=0
  ) -> None:

符号あり8bit整数型 ``int8`` のデータを格納する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (int)``: データ
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

set_int16
^^^^^^^^^

.. code-block:: python

  def set_int16(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data: int,
    stamp_sec: int=0,
    stamp_nsec: int=0
  ) -> None:

符号あり16bit整数型 ``int16`` のデータを格納する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (int)``: データ
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

set_int32
^^^^^^^^^

.. code-block:: python

  def set_int32(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data: int,
    stamp_sec: int=0,
    stamp_nsec: int=0
  ) -> None:

符号あり32bit整数型 ``int32`` のデータを格納する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (int)``: データ
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

set_int64
^^^^^^^^^

.. code-block:: python

  def set_int64(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data: int,
    stamp_sec: int=0,
    stamp_nsec: int=0
  ) -> None:

符号あり64bit整数型 ``int64`` のデータを格納する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (int)``: データ
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

set_float16
^^^^^^^^^^^

.. code-block:: python

  def set_float16(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data: float,
    stamp_sec: int=0,
    stamp_nsec:int=0
  ) -> None:

16bit浮動小数点型 ``float16`` のデータを格納する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (float)``: データ
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

set_float32
^^^^^^^^^^^

.. code-block:: python

  def set_float32(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data: float,
    stamp_sec: int=0,
    stamp_nsec:int=0
  ) -> None:

32bit浮動小数点型 ``float32`` のデータを格納する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (float)``: データ
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

set_float64
^^^^^^^^^^^

.. code-block:: python

  def set_float64(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data: float,
    stamp_sec: int=0,
    stamp_nsec:int=0
  ) -> None:

64bit浮動小数点型 ``float64`` のデータを格納する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (float)``: データ
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

set_semantic1d
^^^^^^^^^^^^^^

.. code-block:: python

  def set_semantic1d(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data: numpy.ndarray,
    label_tag: str,
    stamp_sec: int=0,
    stamp_nsec: int=0
  ) -> None:

符号なし8bit整数型の1次元ラベル ``semantic1d`` のデータを格納する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (numpy.ndarray)``: ``shape=(N,)``, ``dtype=numpy.uint8`` の1次元ラベルデータ
  * ``label_tag (str)``: 依存するラベルのタグ.
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

画像の格納
----------

set_mono8
^^^^^^^^^

.. code-block:: python

  def set_mono8(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data: numpy.ndarray,
    frame_id: str,
    stamp_sec: int=0,
    stamp_nsec: int=0
  ) -> None:

符号なし8bit整数型のモノクロ画像 ``mono8`` のデータを格納する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (numpy.ndarray)``: ``shape=(H, W)``, ``dtype=numpy.uint8`` の画像データ
  * ``frame_id (str)``: 座標系
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

set_mono16
^^^^^^^^^^

.. code-block:: python

  def set_mono16(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data: numpy.ndarray,
    frame_id: str,
    stamp_sec: int=0,
    stamp_nsec: int=0
  ) -> None:

符号なし16bit整数型のモノクロ画像 ``mono16`` のデータを格納する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (numpy.ndarray)``: ``shape=(H, W)``, ``dtype=numpy.uint16`` の画像データ
  * ``frame_id (str)``: 座標系
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

set_bgr8
^^^^^^^^

.. code-block:: python

  def set_bgr8(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data: numpy.ndarray,
    frame_id: str,
    stamp_sec: int=0,
    stamp_nsec: int=0
  ) -> None:

符号なし8bit整数型の3ch BGRカラー画像 ``bgr8`` のデータを格納する.
OpenCVで読み込んだカラー画像の格納に適する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (numpy.ndarray)``: ``shape=(H, W, 3)``, ``dtype=numpy.uint8`` の画像データ
  * ``frame_id (str)``: 座標系
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

set_rgb8
^^^^^^^^

.. code-block:: python

  def set_rgb8(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data: numpy.ndarray,
    frame_id: str,
    stamp_sec: int=0,
    stamp_nsec: int=0
  ) -> None:

符号なし8bit整数型の3ch RGBカラー画像 ``rgb8`` のデータを格納する.
PILで読み込んだカラー画像の格納に適する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (numpy.ndarray)``: ``shape=(H, W, 3)``, ``dtype=numpy.uint8`` の画像データ
  * ``frame_id (str)``: 座標系
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

set_bgra8
^^^^^^^^^

.. code-block:: python

  def set_bgra8(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data: numpy.ndarray,
    frame_id: str,
    stamp_sec: int=0,
    stamp_nsec: int=0
  ) -> None:

符号なし8bit整数型の4ch BGRAカラー画像 ``bgr8`` のデータを格納する.
OpenCVで読み込んだ透過カラー画像の格納に適する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (numpy.ndarray)``: ``shape=(H, W, 4)``, ``dtype=numpy.uint8`` の画像データ
  * ``frame_id (str)``: 座標系
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

set_rgba8
^^^^^^^^^

.. code-block:: python

  def set_rgba8(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data: numpy.ndarray,
    frame_id: str,
    stamp_sec: int=0,
    stamp_nsec: int=0
  ) -> None:

符号なし8bit整数型の4ch RGBAカラー画像 ``rgb8`` のデータを格納する.
PILで読み込んだ透過カラー画像の格納に適する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (numpy.ndarray)``: ``shape=(H, W, 4)``, ``dtype=numpy.uint8`` の画像データ
  * ``frame_id (str)``: 座標系
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

set_depth
^^^^^^^^^

.. code-block:: python

  def set_depth(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data: numpy.ndarray,
    frame_id: str,
    stamp_sec: int=0,
    stamp_nsec: int=0
  ) -> None:

32bit浮動小数点型の深度マップ ``depth`` のデータを格納する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (numpy.ndarray)``: ``shape=(H, W)``, ``dtype=numpy.float32`` の画像データ
  * ``frame_id (str)``: 座標系
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

set_disparity
^^^^^^^^^^^^^

.. code-block:: python

  def set_disparity(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data: numpy.ndarray,
    frame_id: str,
    base_line: float,
    stamp_sec: int=0,
    stamp_nsec: int=0
  ) -> None:

32bit浮動小数点型の視差マップ ``disparity`` のデータを格納する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (numpy.ndarray)``: ``shape=(H, W)``, ``dtype=numpy.float32`` の画像データ
  * ``frame_id (str)``: 座標系
  * ``base_line (float)``: ステレオカメラのベースライン. 単位は画像データの単位と同じにする.
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

set_semantic2d
^^^^^^^^^^^^^^

.. code-block:: python

  def set_semantic2d(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data: numpy.ndarray,
    frame_id: str,
    label_tag: str,
    stamp_sec: int=0,
    stamp_nsec: int=0
  ) -> None:

符号なし8bit整数型の2次元ラベル ``semantic2d`` のデータを格納する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (numpy.ndarray)``: ``shape=(H, W)``, ``dtype=numpy.uint8`` の2次元ラベルデータ
  * ``frame_id (str)``: 座標系
  * ``label_tag (str)``: 依存するラベルのタグ.
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

点群の格納
----------

set_points
^^^^^^^^^^

.. code-block:: python

  def set_points(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data: numpy.ndarray,
    frame_id: str,
    stamp_sec: int=0,
    stamp_nsec: int=0,
    map_id: str=None
  ) -> None:

32bit浮動小数点型の点群 ``points`` のデータを格納する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (numpy.ndarray)``: ``shape=(N, 3)``, ``dtype=numpy.float32`` の点群データ
  * ``frame_id (str)``: 座標系
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .
  * ``map_id (str, optional)``: 三次元点群地図のID. 三次元点群地図として使用する場合は必須. 既定値: ``None``

set_voxel_points
^^^^^^^^^^^^^^^^

.. code-block:: python

  def set_voxel_points(
    h5group: Union[h5py.Group, h5py.File],
    tag: str,
    data: numpy.ndarray,
    frame_id: str,
    voxel_size: float,
    voxels_min: Tuple[float, float, float],
    voxels_max: Tuple[float, float, float],
    voxels_center: Tuple[float, float, float],
    voxels_origin: Tuple[int, int, int],
    label_tag: str=None,
    stamp_sec: int=0,
    stamp_nsec: int=0,
    map_id: str=None
  ) -> None:

Voxelに格納された32bit浮動小数点型の点群 ``voxel-points`` のデータを格納する.
https://github.com/shikishima-TasakiLab/pointsmap-python の ``VoxelGridMap`` データに準拠.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (numpy.ndarray)``: VoxelGridMap (``compound(N,)['x', 'y', 'z']`` を格納したNumpy(Z, Y, X)行列)
  * ``frame_id (str)``: 座標系
  * ``voxel_size (float)``: Voxelのサイズ
  * ``voxels_min (Tuple[float, float, float])``: VoxelGridMapの範囲の最小値 (z_min, y_min, x_min)
  * ``voxels_max (Tuple[float, float, float])``: VoxelGridMapの範囲の最大値 (z_max, y_max, x_max)
  * ``voxels_center (Tuple[float, float, float])``: VoxelGridMapの中心座標 (z_center, y_center, x_center)
  * ``voxels_origin (Tuple[int, int, int])``: VoxelGridMapの中心のVoxelのインデックス (z_origin, y_origin, x_origin)
  * ``label_tag (str, optional)``: 依存するラベルのタグ. 既定値: ``None``
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .
  * ``map_id (str, optional)``: 三次元点群地図のID. 三次元点群地図として使用する場合は必須. 既定値: ``None``

set_semantic3d
^^^^^^^^^^^^^^

.. code-block:: python

  def set_semantic3d(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data_points: numpy.ndarray,
    data_semantic1d: numpy.ndarray,
    frame_id: str,
    label_tag: str,
    stamp_sec: int=0,
    stamp_nsec: int=0,
    map_id: str=None
  ) -> None:

32bit浮動小数点型の点群と, 符号なし8bit整数型の1次元ラベルから成る, ラベル付三次元点群 ``semantic3d`` のデータを格納する.
https://github.com/shikishima-TasakiLab/pointsmap-python の ``Points`` データに準拠.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data_points (numpy.ndarray)``: ``shape=(N, 3)``, ``dtype=numpy.float32`` の点群データ
  * ``data_semantic1d (numpy.ndarray)``: ``shape=(N,)``, ``dtype=numpy.uint8`` の1次元ラベルデータ
  * ``frame_id (str)``: 座標系
  * ``label_tag (str)``: 依存するラベルのタグ.
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .
  * ``map_id (str, optional)``: 三次元点群地図のID. 三次元点群地図として使用する場合は必須. 既定値: ``None``

set_voxel_semantic3d
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  def set_voxel_semantic3d(
    h5group: Union[h5py.Group, h5py.File],
    tag: str,
    data: numpy.ndarray,
    frame_id: str,
    voxel_size: float,
    voxels_min: Tuple[float, float, float],
    voxels_max: Tuple[float, float, float],
    voxels_center: Tuple[float, float, float],
    voxels_origin: Tuple[int, int, int],
    label_tag: str=None,
    stamp_sec: int=0,
    stamp_nsec: int=0,
    map_id: str=None
  ) -> None:

32bit浮動小数点型の点群と, 符号なし8bit整数型の1次元ラベルから成る, Voxelに格納されたラベル付三次元点群 ``voxel-semantic3d`` のデータを格納する.
https://github.com/shikishima-TasakiLab/pointsmap-python の ``VoxelGridMap`` データに準拠.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (numpy.ndarray)``: VoxelGridMap (``compound(N,)['x', 'y', 'z']`` を格納したNumpy(Z, Y, X)行列)
  * ``frame_id (str)``: 座標系
  * ``voxel_size (float)``: Voxelのサイズ
  * ``voxels_min (Tuple[float, float, float])``: VoxelGridMapの範囲の最小値 (z_min, y_min, x_min)
  * ``voxels_max (Tuple[float, float, float])``: VoxelGridMapの範囲の最大値 (z_max, y_max, x_max)
  * ``voxels_center (Tuple[float, float, float])``: VoxelGridMapの中心座標 (z_center, y_center, x_center)
  * ``voxels_origin (Tuple[int, int, int])``: VoxelGridMapの中心のVoxelのインデックス (z_origin, y_origin, x_origin)
  * ``label_tag (str, optional)``: 依存するラベルのタグ. 既定値: ``None``
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .
  * ``map_id (str, optional)``: 三次元点群地図のID. 三次元点群地図として使用する場合は必須. 既定値: ``None``

その他データの格納
------------------

set_pose
^^^^^^^^

.. code-block:: python

  def set_pose(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data_translation: numpy.ndarray,
    data_quaternion: numpy.ndarray,
    frame_id: str,
    child_frame_id: str,
    stamp_sec: int=0,
    stamp_nsec: int=0
  ) -> None:

親座標系→子座標系 の並進ベクトルとクォータニオンから成る ``pose`` のデータを格納する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data_translation (numpy.ndarray)``: ``[tx, ty, tz]``, ``dtype=numpy.float32 or numpy.float64`` の並進ベクトル (親座標系→子座標系)
  * ``data_quaternion (numpy.ndarray)``: ``[qx, qy, qz, qw]``, ``dtype=numpy.float32 or numpy.float64`` のクォータニオン (親座標系→子座標系)
  * ``frame_id (str)``: 親の座標系
  * ``child_frame_id (str)``: 子の座標系
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

set_translation
^^^^^^^^^^^^^^^

.. code-block:: python

  def set_translation(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data: numpy.ndarray,
    stamp_sec: int=0,
    stamp_nsec: int=0
  ) -> None:

並進ベクトル ``translation`` のデータを格納する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (numpy.ndarray)``: ``[tx, ty, tz]``, ``dtype=numpy.float32 or numpy.float64`` の並進ベクトル (親座標系→子座標系)
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

set_quaternion
^^^^^^^^^^^^^^

.. code-block:: python

  def set_quaternion(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data: numpy.ndarray,
    stamp_sec: int=0,
    stamp_nsec: int=0
  ) -> None:

クォータニオン ``quaternion`` のデータを格納する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data (numpy.ndarray)``: ``[qx, qy, qz, qw]``, ``dtype=numpy.float32 or numpy.float64`` のクォータニオン (親座標系→子座標系)
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

set_intrinsic
^^^^^^^^^^^^^

.. code-block:: python

  def set_intrinsic(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data_fx: float,
    data_fy: float,
    data_cx: float,
    data_cy: float,
    data_height: int,
    data_width: int,
    frame_id: str,
    stamp_sec: int=0,
    stamp_nsec: int=0
  ) -> None:

カメラ行列 ``intrinsic`` のデータを格納する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data_fx (float)``: Fx 焦点距離 (水平方向) [px]
  * ``data_fy (float)``: Fy 焦点距離 (垂直方向) [px]
  * ``data_cx (float)``: Cx 画像の光学中心 (水平方向) [px]
  * ``data_cy (float)``: Cy 画像の光学中心 (垂直方向) [px]
  * ``data_height (int)``: 画像の縦幅 [px]
  * ``data_width (int)``: 画像の横幅 [px]
  * ``frame_id (str)``: 座標系
  * ``stamp_sec (int, optional)``: データのタイムスタンプ (整数部[sec]). 既定値: ``0`` .
  * ``stamp_nsec (int, optional)``: データのタイムスタンプ (小数部[nsec]). 既定値: ``0`` .

set_color
^^^^^^^^^

.. code-block:: python

  def set_color(
    h5_group: Union[h5py.Group, h5py.File],
    tag: str,
    data_r: int,
    data_g: int,
    data_b: int
  ) -> None:

色 ``color`` のデータを格納する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``tag (str)``: データのタグ
  * ``data_r (int)``: 赤 [0-255]
  * ``data_g (int)``: 緑 [0-255]
  * ``data_b (int)``: 青 [0-255]

set_label_config
^^^^^^^^^^^^^^^^

.. code-block:: python

  def set_label_config(
    h5_group: Union[h5py.Group, h5py.File],
    index: int,
    name: str,
    data_r: int,
    data_g: int,
    data_b: int
  ) -> None:

ラベルの設定を格納する.

* Args:

  * ``h5_group (h5py.Group, h5py.File)``: データを格納するグループ
  * ``index (int)``: ラベルのインデックス
  * ``name (str)``: ラベルの名前
  * ``data_r (int)``: 赤 [0-255]
  * ``data_g (int)``: 緑 [0-255]
  * ``data_b (int)``: 青 [0-255]

* 実装例:

  .. code-block:: python

    from h5datacreator import H5Dataset
    import numpy as np
    import cv2

    h5file = H5Dataset(path='sample.hdf5')

    # '/data/0/segmentation'に画像を格納する
    h5data: h5py.Group = h5file.get_next_data_group()
    img: np.ndarray = cv2.imread('label.png', cv2.IMREAD_UNCHANGED)
    set_bgr8(
      h5_group=h5data,
      tag='segmentation',
      data=img,
      frame_id='camera'
    )

    label_group = h5file.get_label_group('label')
    set_label_config(label_group, index=0, name='void', data_r=0, data_g=0, data_b=0)

    h5file.close()
