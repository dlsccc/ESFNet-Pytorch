import os
from configparser import ConfigParser
import configparser

"""
    # section distinguish the upper and lower letters, but key and value do not.  节区分大小写，但是键和值不区分大小写。
    The information in the configuration always store the data in string format, it will have translation when reading. 配置文件信息存储为字符串格式，当读取时需要转换格式。
    [DEFAULT]: the value in [DEFAULT] offer default_value to all sections, and it owns the highest priority.    配置文件中的"[DEFAULT]"节提供了默认值，它将对所有节有效，并具有最高优先级。也就是说，如果某个节中没有定义某个键的值，那么它将从"[DEFAULT]"节中获取默认值。
    get: getboolean() getint() getfloat()
    get方法 提供一个更复杂的界面 保持向后兼容性 可以回退关键字仅提供回退值
    fallback 回退值    get方法提供了fallback（回退）参数，用于在未找到指定键时提供回退值，以确保不会出现异常。
    
    refer values in other sections
    interpolation method: configparser.BasicInterpolation()
                          configparser.ExtendedInterpolation() ${section:key}   
                          配置文件中的某个节可以引用其他节中的值。这种引用的方式是使用插值方法。
                          标准的插值方法为configparser.BasicInterpolation()，
                          扩展插值方法为configparser.ExtendedInterpolation()。
                          使用扩展插值方法时，可以使用${section:key}的形式引用其他节中的键值。
    config.set          config.set方法用于在程序中设置配置文件的键值对。
    config.write        config.write方法用于将更新后的配置文件写回到磁盘上，以保存配置文件的修改。
"""
class MyConfiguration():
    def __init__(self, config_file=None):
        super(MyConfiguration, self).__init__()            #感觉这里没必要写super？######

        # ./ current directory
        if config_file is None:
            # 获取当前脚本所在的绝对路径
            current_path = os.path.abspath(os.path.dirname(__file__))
            # 将配置文件的相对路径与当前路径拼接
            config_file = os.path.join(current_path, 'config.cfg')

        config = ConfigParser()
        # interpolation method
        config._interpolation = configparser.ExtendedInterpolation()
        
        #Specify the encooding to utf-8 to avoid UnicodeDecodeError
        #with open(config_file,'r',encoding='utf-8') as f:
        #    config.read_file(f)

        config.read(filenames= config_file)

        self.config = config
        self.config_path = config_file
        self.add_section = 'Additional'
        print("Loaded config file successfully ...")
        #print(len(self.config.sections()))
        for section in self.config.sections():
            for k, v in self.config.items(section):
                print(k, ":", v)

        # TODO make save dir

        config.write(open(config_file, 'w'))

    def add_args(self, key, value):
        self.config.set(self.add_section, key, value)
        self.config.write(open(self.config_path, 'w'))

    # string int float boolean
    @property
    def test_dir(self):
        return self.config.get("Directory", "test_dir")

    @property
    def test_log_dir(self):
        return self.config.get("Directory", "test_log_dir")

    @property
    def pred_dir(self):
        return self.config.get("Directory", "pred_dir")

    @property
    def root_dir(self):
        return self.config.get("Directory", "root_dir")

    @property
    def save_dir(self):
        return self.config.get("Directory", "save_dir")

    @property
    def log_dir(self):
        return self.config.get("Directory", "log_dir")

    @property
    def pred_dir(self):
        return self.config.get("Directory", "pred_dir")

    @property
    def trainset_dir(self):
        return self.config.get("Directory", "trainset_dir")

    @property
    def validset_dir(self):
        return self.config.get("Directory", "validset_dir")

    @property
    def testset_dir(self):
        return self.config.get("Directory", "testset_dir")

    @property
    def data_folder_name(self):
        return self.config.get("Directory", "data_folder_name")

    @property
    def target_folder_name(self):
        return self.config.get("Directory", "target_folder_name")

    @property
    def batch_size(self):
        return self.config.getint("Data", "batch_size")

    @property
    def nb_classes(self):
        return self.config.getint("Data", "nb_classes")

    @property
    def original_size(self):
        return self.config.getint("Data", "original_size")

    @property
    def cropped_size(self):
        return self.config.getint("Data", "cropped_size")
    
    @property
    def step_x(self):
        return self.config.getint("Data", "step_x")
    
    @property
    def step_y(self):
        return self.config.getint("Data", "step_y")

    @property
    def input_size(self):
        return self.config.getint("Data", "input_size")

    @property
    def overlapped(self):
        return self.config.getint("Data", "overlapped")

    @property
    def use_gpu(self):
        return self.config.getboolean("General", "use_gpu")

    @property
    def use_multi_gpus(self):
        return self.config.getboolean("General", "use_multi_gpus")

    @property
    def device_id(self):
        return self.config.getint("General", "device_id")

    @property
    def random_seed(self):
        return self.config.getint("General", "random_seed")

    @property
    def num_workers(self):
        return self.config.getint("General", "num_workers")

    @property
    def lr_algorithm(self):
        return self.config.get("Optimizer", "lr_algorithm")

    @property
    def init_lr(self):
        return self.config.getfloat("Optimizer", "init_lr")

    @property
    def lr_decay(self):
        return self.config.getfloat("Optimizer", "lr_decay")

    @property
    def momentum(self):
        return self.config.getfloat("Optimizer", "momentum")

    @property
    def weight_decay(self):
        return self.config.getfloat("Optimizer", "weight_decay")

    @property
    def epsilon(self):
        return self.config.getfloat("Optimizer", "epsilon")

    @property
    def monitor(self):
        return self.config.get("Train", "monitor")

    @property
    def dis_period(self):
        return self.config.getint("Train", "dis_period")

    @property
    def init_algorithm(self):
        return self.config.get("Train", "init_algorithm")

    @property
    def loss(self):
        return self.config.get("Train", "loss")

    @property
    def pre_trained(self):
        return self.config.getboolean("Train", "pre_trained")

    @property
    def visualization(self):
        return self.config.getboolean("Train", "visualization")

    @property
    def verbosity(self):
        return self.config.getint("Train", "verbosity")

    @property
    def early_stop(self):
        return self.config.getint("Train", "early_stop")

    @property
    def save_period(self):
        return self.config.getint("Train", "save_period")

    @property
    def epochs(self):
        return self.config.getint("Train", "epochs")





if __name__ == '__main__':
    config = MyConfiguration()
    print(config.root_dir)



