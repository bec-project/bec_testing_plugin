from bec_server.scan_server.scans import position_generators
from bec_server.scan_server.scans.grid_scan import GridScan, scan_hook


class DeviceProgressScan(GridScan):
    """A scan that simulates device progress updates."""

    scan_name = "device_progress_grid_scan"

    @scan_hook
    def prepare_scan(self):
        """
        Prepare the scan. This can include any steps that need to be executed
        before the scan is opened, such as preparing the positions (if not done already)
        or setting up the devices.
        """
        self.positions = position_generators.nd_grid_positions(
            self.motor_input_bundles.values(), snaked=self.snaked
        )

        if self.relative:
            self.start_positions = self.components.get_start_positions(self.motors)
            self.positions += self.start_positions

        self.components.check_limits(self.motors, self.positions)

        self.update_scan_info(
            positions=self.positions,
            num_points=len(self.positions),
            num_monitored_readouts=len(self.positions) * self.burst_at_each_point,
        )

        self.actions.add_scan_report_instruction_device_progress(device="waveform")

        self._baseline_readout_status = self.actions.read_baseline_devices(wait=False)

        self._premove_motor_status = self.actions.set(self.motors, self.positions[0], wait=False)
