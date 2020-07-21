import extract as extract_layer
import load as load_layer
import transform as transform_layer
import multiprocessing as m


if __name__ == "__main__":
    # Extract:
    jobs = []
    dates = extract_layer.set_date_range((2016, 2019), (1, 12))
    ibge_codes = extract_layer.get_ibge_codes("csv/municipios_IBGE.csv", "SE")

    for i in range(0, 10):
        process = m.Process(target=extract_layer.gather_data, args=(
            dates, ibge_codes, "JSON/data.json"))
        jobs.append(process)

    for job in jobs:
        job.start()

    for job in jobs:
        job.join()

    print("Extraction process complete.")

    # Transform:
    transform_layer.get_time_dimension(
        (2016, 2020), (1, 13), "csv/time_dimension.csv")
    transform_layer.get_city_dimension("csv/municipios_IBGE.csv",
                                       "csv/city_dimension.csv", "SE")
    transform_layer.get_fate_dimension(
        "JSON/data.json", "csv/fate_dimension.csv")

    print("Transform process complete.")

    # Load:
    # TODO
