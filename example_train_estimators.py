from mleap.data import Data
from mleap.data.estimators import instantiate_default_estimators
from mleap.experiments import Orchestrator


if __name__ == "__main__":
    data = Data()

    input_io = data.open_hdf5('data/delgado.hdf5', mode='r')
    out_io = data.open_hdf5('data/classification.hdf5', mode='a')
    dts_names_list, dts_names_list_full_path = data.list_datasets(hdf5_io=input_io, hdf5_group='delgado_datasets/')
    split_dts_list = data.split_datasets(hdf5_in=input_io, hdf5_out=out_io, dataset_paths=dts_names_list_full_path[0:5])
    instantiated_models = instantiate_default_estimators(estimators=['Classification'], verbose=1)
    orchest = Orchestrator(hdf5_input_io=input_io, 
                           hdf5_output_io=out_io, 
                           original_datasets_group_h5_path='delgado_datasets/',
                           input_io_datasets_loc=dts_names_list_full_path,
                           output_io_split_idx_loc=split_dts_list)
    orchest.run(modelling_strategies=instantiated_models)


